import pygame


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image


BG = (50, 50, 50)
BLACK = (0, 0, 0)

# sprite sheet dog: --------------------------------------------------
sprite_sheet_image_dog_idle = pygame.image.load(
    "assets\street-animal\\1 Dog\Idle.png"
).convert_alpha()
sprite_sheet_dog_idle = spritesheet.SpriteSheet(sprite_sheet_image_dog_idle)
frame_arr_dog_idle = [
    sprite_sheet_dog_idle.get_image(i, 48, 48, 3, BLACK) for i in range(4)
]

sprite_sheet_image_dog_walk = pygame.image.load(
    "assets\street-animal\\1 Dog\Walk.png"
).convert_alpha()
sprite_sheet_dog_walk = spritesheet.SpriteSheet(sprite_sheet_image_dog_walk)
frame_arr_dog_walk = [
    sprite_sheet_dog_walk.get_image(i, 48, 48, 3, BLACK) for i in range(4)
]

# sprite sheet cat: --------------------------------------------------
sprite_sheet_image_cat_idle = pygame.image.load(
    "assets\street-animal\\3 Cat\Idle.png"
).convert_alpha()
sprite_sheet_cat_idle = spritesheet.SpriteSheet(sprite_sheet_image_cat_idle)
frame_arr_cat_idle = [
    sprite_sheet_cat_idle.get_image(i, 48, 48, 3, BLACK) for i in range(4)
]

sprite_sheet_image_cat_walk = pygame.image.load(
    "assets\street-animal\\3 Cat\Walk.png"
).convert_alpha()
sprite_sheet_cat_walk = spritesheet.SpriteSheet(sprite_sheet_image_cat_walk)
frame_arr_cat_walk = [
    sprite_sheet_cat_walk.get_image(i, 48, 48, 3, BLACK) for i in range(4)
]
