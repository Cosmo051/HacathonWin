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
DOG_SPRITE_WIDTH = 48
CAT_SPRITE_WIDTH = 48
WORLD_LIMIT_LEFT = 10
WORLD_LIMIT_RIGHT = 3000

CRIS_WIDTH = 48
CRIS_HEIGHT = 48
BITCH_MUSIC = "assets\music\\bg_beach_m.mp3"
MUSHROOM_TRANS = "assets\music\\bg_music.mp3"
SCARY_SOUND = "assets\music\\bg_h_music.mp3"
SAGOL_SOUND = "assets\music\\bg_music.mp3"