import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432
BG = (50, 50, 50)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")

# background code---------------------------------------------------------
# define game variables
scroll = 0
bg_index = 2

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

    # get keypresses
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    if key[pygame.K_RIGHT] and scroll < 3000:
        scroll += 5

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
