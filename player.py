from constants import *
import pygame
from spritesheet import *
class Player:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.y_gravity = 4
        self.min_y = GROUND_LEVEL
        self.jump_height = 30
        self.y_velocity = self.jump_height
        self.width = width * (SCALE - 1)
        self.height = height * (SCALE - 1)
        self.is_colieded = False
        self.rect = pygame.Rect(x, y + height, self.width, self.height)
        self.horiz_speed = 50
        self.frames_dic = {
            "Idle": init_sprite(f"assets\street-animal\{name}\Idle.png"),
            "Walk": init_sprite(f"assets\street-animal\{name}\Walk.png"),
            "WalkBack": flip_images(
                init_sprite(f"assets\street-animal\{name}\Walk.png")
            ),
        }

    def draw_rect(self, window):
        pygame.draw.rect(window, "black", self.rect)

    def set_y(self, y):
        self.y = y - self.height

    def update(self):
        self.rect = pygame.Rect(self.x, self.y + (self.height/(SCALE - 1)), self.width, self.height)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_rect(self):
        return self.rect

    def get_frames_dic(self):
        return self.frames_dic

    def draw(self, screen, state, index):
        screen.blit(self.frames_dic[state][index], (self.x, self.y))

    def move_x(self, state, border):
        if (state == -1 and self.x > WORLD_LIMIT_LEFT) or (state == 1 and self.x < border):
            self.x += self.horiz_speed * state
        self.update()
    
    def move_x_with_stick(self, horiz_move, border):
        if (horiz_move < 0 and self.x > WORLD_LIMIT_LEFT) or (horiz_move > 0 and self.x < border):
            self.x += int(horiz_move * self.horiz_speed)
        self.update()
        

def flip_images(img_arr):
    flipped_arr = []
    for img in img_arr:
        flipped_img = pygame.transform.flip(img, True, False).convert_alpha()
        flipped_arr.append(flipped_img)
    return flipped_arr