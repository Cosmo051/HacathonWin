import pygame
class Platform:
     # type: ignore
    def __init__(self, img_path, width, height, x, y):
        self.img = pygame.transform.scale(pygame.image.load(img_path), (width, height))
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def get_rect(self):
        rect = self.img.get_rect()
        rect.topleft = (self.x, self.y)
        return rect