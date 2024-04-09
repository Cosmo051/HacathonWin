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

def init_sprite(path):
    # sprite sheet dog: --------------------------------------------------
	sprite_sheet_image = pygame.image.load(path).convert_alpha()
	sprite_sheet = SpriteSheet(sprite_sheet_image)
	frame_arr = [sprite_sheet.get_image(i, 48, 48, 3, BLACK) for i in range(4)]
	return frame_arr


