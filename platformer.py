import pygame
from player import *
class Platform:
     # type: ignore
    def __init__(self, img_path, width, height, x, y):
        self.img = pygame.transform.scale(pygame.image.load(img_path), (width, height))
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
    
    def get_rect(self):
        self.rect.topleft = (self.x, self.y)
        return self.rect
    
    def update_plat_rect(self, offset):
        self.rect.move_ip(-offset, 0)
    
    def player_on_platform(self, player:Player):
        plat = self.get_rect()
        if plat.colliderect(player.get_rect()) and (plat.y <= (player.y + player.height) <= (plat.y + (plat.height//2))):
            #player.y = self.rect.top - player.height # +1 for fixing player wiggle 
            player.update()
            return True
        return False
    
    def draw_rect(self, window):
        pygame.draw.rect(window, "black", self.rect)
    
    def draw(self, screen:pygame.Surface, offset):
        screen.blit(self.img, (self.x - offset, self.y))
        self.update_plat_rect(offset)