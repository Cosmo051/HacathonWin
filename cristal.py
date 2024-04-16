import pygame
from constants import *
class Cristal:
    def __init__(self, x, y, width, height, path, kind): 
        self.x = x
        self.y = y
        self.root_y = y
        self.width = width
        self.height = height
        self.path = path
        self.kind = kind #dog cristal or cat cristal
        self.is_collected = False
        self.range_of_movement = 10  # Define the range of movement
        self.step = 1  # Define the step for movement
    
    def get_X(self):
        return self.x
    
    def set_x(self, x):
        self.x = x
    
    def get_y(self):
        return self.y
    
    def set_y(self, y):
        self.y = y
    
    def move(self):
        # Adjust y position within range_of_movement
        if self.y <= self.root_y - self.range_of_movement or self.y >= self.root_y + self.range_of_movement:
            self.step = -self.step  # Reverse direction when reaching boundaries
        self.y += self.step

    def draw(self, screen):
        img = pygame.image.load(self.path)
        img = pygame.transform.scale(img, (self.width, self.height))
        screen.blit(img, (self.x, self.y))
    

