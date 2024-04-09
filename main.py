import pygame
from spritesheet import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432
BG = (50, 50, 50)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Eternal")


# background code---------------------------------------------------------
# define game variables
scroll = 0
bg_index = 3

ground_image = pygame.image.load(
    f"assets/backgrounds-assets/_PNG/{bg_index}/1.png"
).convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(7, 1, -1):
    bg_image = pygame.image.load(
        f"assets/backgrounds-assets/_PNG/{bg_index}/{i}.png"
    ).convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()


def draw_bg():
    for x in range(5):
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
            speed += 0.2


def draw_ground():
    for x in range(15):
        screen.blit(
            ground_image,
            ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height),
        )




frame_arr_dog_idle = init_sprite("assets\street-animal\\1 Dog\Idle.png")
frame_arr_cat_idle = init_sprite("assets\street-animal\\3 Cat\Idle.png")
frame_arr_dog_walk = init_sprite("assets\street-animal\\1 Dog\Walk.png")
frame_arr_cat_walk = init_sprite("assets\street-animal\\3 Cat\Walk.png")

clock = pygame.time.Clock()
run = True
i = 0
state_dog = 0
state_cat = 0
while run:
    clock.tick(10)
    # update background
    screen.fill(BG)

    # draw world
    draw_bg()
    draw_ground()
    
    key = pygame.key.get_pressed()
    # get keypresses
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    if key[pygame.K_RIGHT] and scroll < 3000:
        scroll += 5

    # state handling----------------
    if key[pygame.K_a]:
        state_dog = 1
        scroll += 5
    else:
        state_dog = 0

    if key[pygame.K_l]:
        state_cat = 1
        scroll += 5
    else:
        state_cat = 0

    # show frame image
    match state_dog:
        case 0:
            screen.blit(frame_arr_dog_idle[i], (0, 200))
        case 1:
            screen.blit(frame_arr_dog_walk[i], (0, 200))

    match state_cat:
        case 0:
            screen.blit(frame_arr_cat_idle[i], (100, 200))
        case 1:
            screen.blit(frame_arr_cat_walk[i], (100, 200))
    i += 1
    if i >= len(frame_arr_dog_idle):
        i = 0

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
