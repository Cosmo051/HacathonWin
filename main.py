import pygame
from spritesheet import *
from constants import *
from network import Network
from platformer import *

pygame.init()
#connect the sprite to the class
class Player:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.frames_dic = {"Idle": init_sprite(f"assets\street-animal\{name}\Idle.png"), "Walk": init_sprite(f"assets\street-animal\{name}\Walk.png"), "WalkBack":flip_images(init_sprite(f"assets\street-animal\{name}\Walk.png"))}
    
    def draw_rect(self, window):
        pygame.draw.rect(window, self.rect)
    
    def set_y(self, y):
        self.y = y
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
    def get_x(self):
        return self.x
    def get_rect(self):
        return self.rect
    def get_frames_dic(self):
        return self.frames_dic
    
    def draw(self, screen, state, index):
        screen.blit(self.frames_dic[state][index], (self.x, self.y))
    
    def move_x(self, state):
        self.x += SPEED*state
        self.update()



SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 864
BG = (50, 50, 50)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Eternal")

def flip_images(img_arr):
    flipped_arr = []
    for img in img_arr:
        flipped_img = pygame.transform.flip(img, True, False).convert_alpha()
        flipped_arr.append(flipped_img)
    return flipped_arr

# background code---------------------------------------------------------start
# define game variables
scroll = 0
bg_index = 3

ground_image = pygame.image.load(
    f"assets/backgrounds-assets/_PNG/{bg_index}/1.png"
).convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

# creating the platforms for the level
plat_img_path = "assets\platform-img\PNG\Tiles\\tile50.png"
plat = Platform(plat_img_path, 100, 50, 300, 100)
plat2 = Platform(plat_img_path, 200, 10, 100, 20)
plat_lst = [plat, plat2]

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
        draw_platforms(plat_lst, screen, scroll*speed)


def draw_ground():
    for x in range(15):
        screen.blit(
            ground_image,
            ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height),
        )


def draw_platforms(platform_lst:list, screen, offset):
    for plat in platform_lst:
        plat.draw(screen, offset)
# background code---------------------------------------------------------end

#position helper func
def read_pos(str:str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])
#######################################



clock = pygame.time.Clock()
run = True
#server shit
client_number = 0
n = Network()
#start_pos = read_pos(n.get_pos())
##############
i = 0
state_dog = 0
state_cat = 0

dog_x = 0
cat_x = 0

dog_y = 634
cat_y = 634




dog = Player(dog_x, dog_y, 48, 48,"dog")
cat = Player(0, 0, 48, 48,"cat")
dog_img = dog.get_frames_dic()["Idle"][0]
cat_img = cat.get_frames_dic()["Idle"][0]

# collision check
def plat_collision_check(player, platform_lst):
    for plat in platform_lst:
        plat.player_on_platform(player)

while run:
    clock.tick(10)
    # update background
    screen.fill(BG)

    # draw world
    draw_bg()
    draw_ground()
    p2_pos = read_pos(n.send(make_pos((p.x, p.y))))
    p2.x = p2_pos[0]
    p2y = p2_pos[1]
    p2.update()
    key = pygame.key.get_pressed()
    # state handling----------------
    if key[pygame.K_d]:
        state_dog = 1
        if dog.get_x() < WALKING_LIMIT:
            dog.move_x(1)
    elif key[pygame.K_a]:
        state_dog = 2
        if dog.get_x() > 0:
            dog.move_x(-1)
    else:
        state_dog = 0

    if key[pygame.K_l]:
        state_cat = 1
        if cat.get_x() < WALKING_LIMIT:
            cat.move_x(1)
    elif key[pygame.K_j]:
        state_cat = 2
        if cat.get_x() > 0:
            cat.move_x(-1)
    else:
        state_cat = 0
    
    if cat.get_x() > SCREEN_WIDTH/2 and dog.get_x() > SCREEN_WIDTH/2 and key[pygame.K_d] and key[pygame.K_l]:
        scroll += 5
    
    if cat.get_x() < SCREEN_WIDTH/2 and dog.get_x() < SCREEN_WIDTH/2 and key[pygame.K_a] and key[pygame.K_j]:
        scroll -= 5
    
    # show frame image
    match state_dog:
        case 0:
            dog.draw(screen, "Idle", i)
        case 1:
            dog.draw(screen, "Walk", i)
        case 2:
            dog.draw(screen, "WalkBack", i)

    match state_cat:
        case 0:
            cat.draw(screen, "Idle", i)
        case 1:
            cat.draw(screen, "Walk", i)
        case 2:
            cat.draw(screen, "WalkBack", i)
    i += 1
    if i >= len(dog.get_frames_dic()["Idle"]):
        i = 0
    
    #collision handeling
    plat_collision_check(dog, plat_lst)
    plat_collision_check(cat, plat_lst)
        # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
