# import pygame

# def load_image(path, size):
#     img = pygame.image.load(path)
#     img = pygame.transform.scale(img, size)
#     return img


# def mouse_on_image(pos, img, location):
#     rect = img.get_rect()
#     rect.x = location[0]
#     rect.y = location[1]
#     return rect.collidepoint(pos)


# def draw_image(screen, img, location):
#     screen.blit(img, location)

SPEED = 30
SCALE = 3
GRAVITY = 30
GROUND_LEVEL = 634
GROUND_LEVEL_STATIC_BG = 650
DOG_SPRITE_WIDTH = 48
CAT_SPRITE_WIDTH = 48
WALKING_LIMIT = 1500#max X for cat and dog

CRIS_WIDTH = 48
CRIS_HEIGHT = 48