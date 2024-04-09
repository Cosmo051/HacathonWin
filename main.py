import pygame
from spritesheet import *

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")


clock = pygame.time.Clock()
run = True
i = 0
state_dog = 0
state_cat = 0
while run:
    clock.tick(10)
    # update background
    screen.fill(BG)

    # state handling----------------
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        state_dog = 1
    else:
        state_dog = 0

    key = pygame.key.get_pressed()
    if key[pygame.K_l]:
        state_cat = 1
    else:
        state_cat = 0

    # show frame image
    match state_dog:
        case 0:
            screen.blit(frame_arr_dog_idle[i], (0, 0))
        case 1:
            screen.blit(frame_arr_dog_walk[i], (0, 0))

    match state_cat:
        case 0:
            screen.blit(frame_arr_cat_idle[i], (100, 0))
        case 1:
            screen.blit(frame_arr_cat_walk[i], (100, 0))
    i += 1
    if i >= len(frame_arr_dog_idle):
        i = 0

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
