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
    
    def player_on_platform(self, player):
        plat = self.get_rect()
        if plat.colliderect(player.get_rect()):
            player.set_y(self.y)
            return True
        return False
    
    def draw(self, screen:pygame.Surface, offset):
        screen.blit(self.img, (self.x-offset, self.y))