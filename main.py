import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")

sprite_sheet_image = pygame.image.load(
    "assets/doux.png"
).convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)


frame_arr = [sprite_sheet.get_image(i, 24, 24, 3, BLACK) for i in range(24)]
clock = pygame.time.Clock()
run = True
i = 0
while run:
    clock.tick(10)
    # update background
    screen.fill(BG)

    # show frame image
    screen.blit(frame_arr[i], (0, 0))
    i += 1
    if i >= len(frame_arr):
        i = 0

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
