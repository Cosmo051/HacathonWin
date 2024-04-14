import pygame
from spritesheet import *
from constants import *

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 864
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
        #drawing platforms
        screen.blit(plat, (1500-scroll*speed, 200))


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

dog_x = 0
cat_x = 0

dog_y = 634
cat_y = 634
plat = pygame.image.load("assets\platform-img\PNG\Tiles\\tile50.png")
while run:
    clock.tick(10)
    # update background
    screen.fill(BG)

    # draw world
    draw_bg()
    draw_ground()

    key = pygame.key.get_pressed()
    # state handling----------------
    if key[pygame.K_d]:
        state_dog = 1
        if dog_x < WALKING_LIMIT:
            dog_x += SPEED
    elif key[pygame.K_a]:
        state_dog = 2
        if dog_x > 0:
            dog_x -= SPEED
    else:
        state_dog = 0

    if key[pygame.K_l]:
        state_cat = 1
        if cat_x < WALKING_LIMIT:
            cat_x += SPEED
    elif key[pygame.K_j]:
        state_cat = 2
        if cat_x > 0:
            cat_x -= SPEED
    else:
        state_cat = 0
    
    if cat_x > SCREEN_WIDTH/2 and dog_x > SCREEN_WIDTH/2 and key[pygame.K_d] and key[pygame.K_l]:
        scroll += 5
    
    if cat_x < SCREEN_WIDTH/2 and dog_x < SCREEN_WIDTH/2 and key[pygame.K_a] and key[pygame.K_j]:
        scroll -= 5
    
    # show frame image
    match state_dog:
        case 0:
            screen.blit(frame_arr_dog_idle[i], (dog_x, dog_y))
        case 1:
            screen.blit(frame_arr_dog_walk[i], (dog_x, dog_y))
        case 2:
            img = frame_arr_dog_walk[i]
            img = pygame.transform.flip(img, True, False).convert_alpha()# mirroring the image on x axis
            screen.blit(img, (dog_x, dog_y))

    match state_cat:
        case 0:
            screen.blit(frame_arr_cat_idle[i], (cat_x, cat_y))
        case 1:
            screen.blit(frame_arr_cat_walk[i], (cat_x, cat_y))
        case 2:
            img = frame_arr_cat_walk[i]
            img = pygame.transform.flip(img, True, False).convert_alpha()# mirroring the image on x axis
            screen.blit(img, (cat_x, cat_y))
    i += 1
    if i >= len(frame_arr_dog_idle):
        i = 0

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
