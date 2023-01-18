"""Класс пакмана. Функционал: передвижение, отображение, коллизии, начисление очков, активация страха"""
from datetime import datetime
import pygame
from constants import SETTINGS_PATH, RED, YELLOW
from objects.image import ImageObject
from objects.wall import Wall, Empty, TeleportWall
from objects.seed import Seed, BigSeed


class Pacman(ImageObject):
    DEBUG = False
    filename = 'images/pacman/right/1.png'
    image = pygame.image.load(filename)
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    DEFAULT_DIRECTIONS = {
        RIGHT: [1, 0],
        LEFT: [-1, 0],
        UP: [0, -1],
        DOWN: [0, 1],
    }
    path_to_settings = SETTINGS_PATH
    images_right = [pygame.image.load(f'images/pacman/right/{i}.png') for i in (1, 2, 3, 2)]
    images_left = [pygame.image.load(f'images/pacman/left/{i}.png') for i in (1, 2, 3, 2)]
    images_up = [pygame.image.load(f'images/pacman/up/{i}.png') for i in (1, 2, 3, 2)]
    images_down = [pygame.image.load(f'images/pacman/down/{i}.png') for i in (1, 2, 3, 2)]
    image_index = 0

    def __init__(self, game, field, x=0, y=0, direction=RIGHT):
        super().__init__(game)
        self.field = field
        self.rect.center = (x, y)
        self.direction = direction
        self.can_move = True
        self.next_direction = direction
        self.cur_images = {
            self.RIGHT: self.images_right,
            self.LEFT: self.images_left,
            self.UP: self.images_up,
            self.DOWN: self.images_down
        }

        self.last_cadr_time = datetime.now()
        self.movement_keys()
        self.current_cell = [0, 0]
        self.future_cell = [0, 0]

    def animation(self):
        if not self.can_move:
            self.image = self.cur_images[self.direction][2]
            return
        now_time = datetime.now()
        if (now_time - self.last_cadr_time).microseconds > 70000:
            self.image = self.cur_images[self.direction][self.image_index % 4]
            self.last_cadr_time = datetime.now()
            self.image_index += 1

    def movement_keys(self):
        # применение настроек
        if self.game.settings.keys:
            self.buttons = {
                'button_right': pygame.K_d,
                'button_up': pygame.K_w,
                'button_left': pygame.K_a,
                'button_down': pygame.K_s,
            }
        else:
            self.buttons = {
                'button_right': pygame.K_RIGHT,
                'button_up': pygame.K_UP,
                'button_left': pygame.K_LEFT,
                'button_down': pygame.K_DOWN,
            }

    def step(self, back=False):
        if not back:
            directions = Pacman.DEFAULT_DIRECTIONS
            if not self.can_move:
                return
        else:
            # шаг назад (от стены)
            directions = {
                self.RIGHT: [-1, 0],
                self.LEFT: [1, 0],
                self.UP: [0, 1],
                self.DOWN: [0, -1],
            }
        self.move_center(
            self.rect.centerx + directions[self.direction][0],
            self.rect.centery + directions[self.direction][1]
        )

    def reset_position(self, x=18 * 15, y=18 * 24, direction=RIGHT):
        self.rect.centerx = x
        self.rect.centery = y
        self.direction = direction
        self.next_direction = direction

    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.size[0] or self.rect.top < 0 or self.rect.bottom > \
                self.game.size[1]:
            self.reset_position()

    def collide(self):
        near_positions = [
            [self.current_cell[0] - 1, self.current_cell[1]],
            [self.current_cell[0] + 1, self.current_cell[1]],
            [self.current_cell[0], self.current_cell[1] - 1],
            [self.current_cell[0], self.current_cell[1] + 1],
        ]
        for i in range(len(self.field.field)):
            for j in range(len(self.field.field[i])):
                obj = self.field.field[i][j]
                if type(obj) == Wall:
                    if self.rect.colliderect(obj.rect):
                        self.step(back=True)
                        self.can_move = False
                if type(obj) == Seed or type(obj) == BigSeed:
                    if self.rect.collidepoint(obj.rect.center):
                        self.field.update(i, j, Empty)
                        if type(obj) == Seed:
                            self.game.score.increase_on(Seed.POINTS)
                            self.field.seeds_count -= 1
                        else:
                            for ghost in self.game.scenes[self.game.current_scene_index].ghosts:
                                if ghost.state != ghost.STAY_IN:
                                    ghost.frightened_is_active = True
                        self.game.sounds.sounds['waka waka'].play()
                if type(obj) == TeleportWall:
                    if self.rect.colliderect(obj.rect):
                        if self.direction == self.RIGHT:
                            self.reset_position(18 * 2, 18 * 15, self.RIGHT)
                        else:
                            self.reset_position(18 * 27, 18 * 15, self.LEFT)

    def change_direction(self):
        dir = {
            self.RIGHT: pygame.Rect(self.rect.x + 5, self.rect.y, self.rect.w, self.rect.h),
            self.LEFT: pygame.Rect(self.rect.x - 5, self.rect.y, self.rect.w, self.rect.h),
            self.UP: pygame.Rect(self.rect.x, self.rect.y - 5, self.rect.w, self.rect.h),
            self.DOWN: pygame.Rect(self.rect.x, self.rect.y + 5, self.rect.w, self.rect.h)
        }
        for row in self.field.field:
            for item in row:
                if type(item) == Wall:
                    if dir[self.next_direction].colliderect(item.rect):
                        return
        self.direction = self.next_direction

    def process_logic(self):
        self.change_direction()
        self.collide()
        self.step()
        self.animation()
        self.check_borders()  # костыль
        self.get_current_cell()

    def process_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == self.buttons['button_right']:
            self.next_direction = self.RIGHT
        elif event.key == self.buttons['button_left']:
            self.next_direction = self.LEFT
        elif event.key == self.buttons['button_up']:
            self.next_direction = self.UP
        elif event.key == self.buttons['button_down']:
            self.next_direction = self.DOWN
        self.can_move = True

    def process_draw(self):
        super(Pacman, self).process_draw()
        if not self.DEBUG:
            return

        if self.field:
            pygame.draw.rect(self.game.screen, RED, [
                self.current_cell[0] * self.field.CELL_WIDTH + self.field.rect.x,
                self.current_cell[1] * self.field.CELL_WIDTH + self.field.rect.y,
                self.field.CELL_WIDTH,
                self.field.CELL_WIDTH,
            ], 2)
            pygame.draw.rect(self.game.screen, YELLOW, [
                self.future_cell[0] * self.field.CELL_WIDTH + self.field.rect.x,
                self.future_cell[1] * self.field.CELL_WIDTH + self.field.rect.y,
                self.field.CELL_WIDTH,
                self.field.CELL_WIDTH,
            ], 2)

    def get_current_cell(self):
        cell_column = (self.rect.centerx - self.field.rect.x) // self.field.CELL_WIDTH
        cell_row = (self.rect.centery - self.field.rect.y) // self.field.CELL_WIDTH
        self.current_cell = [cell_column, cell_row]
        cell_column += self.DEFAULT_DIRECTIONS[self.direction][0] * 4
        cell_row += self.DEFAULT_DIRECTIONS[self.direction][1] * 4
        self.future_cell = [cell_column, cell_row]
