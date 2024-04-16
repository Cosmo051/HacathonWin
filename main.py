import pygame
import sys
import subprocess
import threading
from spritesheet import *
from constants import *
from network import Network
from platformer import *
from cristal import *
import random

pygame.init()


# connect the sprite to the class
class Player:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.y_gravity = 2
        self.min_y = GROUND_LEVEL
        self.jump_height = 30
        self.y_velocity = self.jump_height
        self.width = width * (SCALE - 1)
        self.height = height * (SCALE - 1)
        self.rect = pygame.Rect(x, y + height, self.width, self.height)
        self.frames_dic = {
            "Idle": init_sprite(f"assets\street-animal\{name}\Idle.png"),
            "Walk": init_sprite(f"assets\street-animal\{name}\Walk.png"),
            "WalkBack": flip_images(
                init_sprite(f"assets\street-animal\{name}\Walk.png")
            ),
        }

    def draw_rect(self, window):
        pygame.draw.rect(window, "black", self.rect)

    def set_y(self, y):
        self.y = y - self.height

    def update(self):
        self.rect = pygame.Rect(self.x, self.y + (self.height/(SCALE - 1)), self.width, self.height)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_rect(self):
        return self.rect

    def get_frames_dic(self):
        return self.frames_dic

    def draw(self, screen, state, index):
        screen.blit(self.frames_dic[state][index], (self.x, self.y))

    def move_x(self, state):
        self.x += SPEED * state
        self.update()


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 864
BG = (50, 50, 50)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Eternal")

#def run_other_file(file_path):
    #try:
        #subprocess.run(['python', file_path], check=True)
    #except subprocess.CalledProcessError as e:
        #print(f"Error running {file_path}: {e}")
        #sys.exit(1)
#server_thread = threading.Thread(target=run_other_file, args="server.py")
#server_thread.start()

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
# List 1
plat_lst_1 = [
    Platform(plat_img_path, 150, 30, 200, 50),
    Platform(plat_img_path, 100, 20, 400, 150),
    Platform(plat_img_path, 120, 40, 600, 250),
    Platform(plat_img_path, 130, 25, 800, 350),
    Platform(plat_img_path, 100, 30, 1000, 450),
    Platform(plat_img_path, 110, 35, 1200, 550),
    Platform(plat_img_path, 140, 25, 1400, 450),
    Platform(plat_img_path, 90, 20, 1600, 350),
    Platform(plat_img_path, 100, 30, 1800, 250),
    Platform(plat_img_path, 120, 25, 2000, 150)
]

# List 2
plat_lst_2 = [
    Platform(plat_img_path, 100, 30, 100, 200),
    Platform(plat_img_path, 120, 25, 300, 300),
    Platform(plat_img_path, 140, 40, 500, 400),
    Platform(plat_img_path, 110, 20, 700, 500),
    Platform(plat_img_path, 130, 35, 900, 400),
    Platform(plat_img_path, 150, 25, 1100, 300),
    Platform(plat_img_path, 100, 30, 1300, 200),
    Platform(plat_img_path, 120, 20, 1500, 100),
    Platform(plat_img_path, 140, 25, 1700, 200),
    Platform(plat_img_path, 110, 40, 1900, 300)
]

# List 3
plat_lst_3 = [
    Platform(plat_img_path, 130, 25, 200, 350),
    Platform(plat_img_path, 140, 30, 400, 250),
    Platform(plat_img_path, 120, 20, 600, 150),
    Platform(plat_img_path, 100, 35, 800, 250),
    Platform(plat_img_path, 110, 40, 1000, 350),
    Platform(plat_img_path, 120, 25, 1200, 450),
    Platform(plat_img_path, 140, 30, 1400, 350),
    Platform(plat_img_path, 130, 20, 1600, 250),
    Platform(plat_img_path, 100, 25, 1800, 150),
    Platform(plat_img_path, 150, 30, 2000, 250)
]

# List 4
plat_lst_4 = [
    Platform(plat_img_path, 120, 25, 100, 500),
    Platform(plat_img_path, 110, 30, 300, 400),
    Platform(plat_img_path, 140, 20, 500, 300),
    Platform(plat_img_path, 130, 35, 700, 200),
    Platform(plat_img_path, 150, 30, 900, 300),
    Platform(plat_img_path, 100, 20, 1100, 400),
    Platform(plat_img_path, 120, 25, 1300, 500),
    Platform(plat_img_path, 140, 30, 1500, 400),
    Platform(plat_img_path, 110, 20, 1700, 300),
    Platform(plat_img_path, 130, 35, 1900, 400)
]

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
        # drawing platforms
        draw_platforms(plat_lst_1, screen, scroll * speed)


def draw_ground():
    for x in range(15):
        screen.blit(
            ground_image,
            ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height),
        )


def draw_platforms(platform_lst: list, screen, offset):
    for plat in platform_lst:
        plat.draw(screen, offset)


# background code---------------------------------------------------------end


# position helper func
def read_pos(str:str):
    str = str.split("_")
    print(str[0])
    return int(str[0]), int(str[1]), str[2], eval(str[3])

def make_pos(tup):
    return str(tup[0]) + "_" + str(tup[1]) + "_" + str(tup[2]) + "_" + str(tup[3])

portal_img = pygame.image.load("assets\\backgrounds-assets\portal.png")

def redrawWindow(window, dog, cat, dog_state, cat_state, index,portal, cris_list_dog1, cris_list_cat1):
    dog.draw(window, dog_state, index)
    cat.draw(window, cat_state, index)
    draw_crystals(window, cris_list_dog1)
    draw_crystals(window, cris_list_cat1)
    portal = pygame.transform.scale(portal, (300, 300))
    screen.blit(portal, (2500, 334))
    pygame.display.update()


#######################################


clock = pygame.time.Clock()
run = True
# server shit
client_number = 0
n = Network()
start_pos = read_pos(n.get_pos())
##############
i = 0
state_dog = start_pos[2]
state_cat = 0
cris_list_cord = start_pos[3]
dog_x = 0
cat_x = 0

dog_y = 634
cat_y = 634


dog = Player(start_pos[0], start_pos[1], 48, 48, "dog")
cat = Player(0, 0, 48, 48, "cat")
dog_img = dog.get_frames_dic()[state_dog][0]
cat_img = cat.get_frames_dic()["Idle"][0]
jumping = False


# collision check
def plat_collision_check(player, platform_lst):
    for plat in platform_lst:
        if plat.player_on_platform(player):
            return True, plat
    player.min_y = GROUND_LEVEL
    return False, None


def gravitational_force(player: Player):
    flag, plat = plat_collision_check(player, plat_lst_1)
    if (not flag) and (player.get_y() < GROUND_LEVEL):
        if player.y + GRAVITY > GROUND_LEVEL:
            player.y = GROUND_LEVEL
        else:
            player.y = player.y + GRAVITY
    elif flag:
        player.y = plat.y - player.height - plat.height



def create_crystals(coor):
    cris_list_created = []
    for i in range(len(coor[0])):
        cris_list_created.append(Cristal(coor[0][i], coor[1][i], CRIS_WIDTH, CRIS_HEIGHT, "assets\cristal assets\PNG\shiny\\4.png", "dog"))
    return cris_list_created

def draw_crystals(screen, cris_list):
    for cris in cris_list:
        cris.draw(screen)

def move_crystals(cris_list):
    for cris in cris_list:
        cris.move()

cris_list_dog = create_crystals(cris_list_cord)
cris_flag = True
while run:
    clock.tick(10)
    # update background
    screen.fill(BG)

    # draw world
    draw_bg()
    draw_ground()
    cat_pos = read_pos(n.send(make_pos((dog.x, dog.y, state_dog, cris_list_cord))))
    cat.x = cat_pos[0]
    cat.y = cat_pos[1]
    state_cat = cat_pos[2]
    cris_list_cat = create_crystals(cat_pos[3])

    cat.update()
    key = pygame.key.get_pressed()
    # state handling----------------
    if key[pygame.K_d]:
        state_dog = "Walk"
        if dog.get_x() < WALKING_LIMIT:
            dog.move_x(1)
    elif key[pygame.K_a]:
        state_dog = "WalkBack"
        if dog.get_x() > 0:
            dog.move_x(-1)
    else:
        state_dog = "Idle"
    
    if key[pygame.K_SPACE]:
        jumping = True
    
    if jumping:
        dog.y -= dog.y_velocity
        dog.y_velocity -= dog.y_gravity
        print(dog.y_velocity)
        dog.update()
        if dog.y_velocity < 0:
            dog.y_velocity = dog.jump_height
            jumping = False
        dog.update()

    if (
        cat.get_x() > SCREEN_WIDTH / 2
        and dog.get_x() > SCREEN_WIDTH / 2
        and key[pygame.K_d]
        and key[pygame.K_l]
    ):
        scroll += 5

    if (
        cat.get_x() < SCREEN_WIDTH / 2
        and dog.get_x() < SCREEN_WIDTH / 2
        and key[pygame.K_a]
        and key[pygame.K_j]
    ):
        scroll -= 5

    # show frame image
    i += 1
    if i >= len(dog.get_frames_dic()["Idle"]):
        i = 0

    # collision handeling
    flag, plat = plat_collision_check(dog, plat_lst_1)
    if flag:
        dog.y = plat.y - dog.height - plat.height

    #create_crystals(screen, cris_list_dog)
    move_crystals(cris_list_dog)


    # Yaniv stuff
    if (not jumping):
        gravitational_force(dog)
        dog.update()
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    dog.update()
    redrawWindow(screen, dog, cat, state_dog, state_cat, i, portal_img, cris_list_cat, cris_list_dog)
    # pygame.display.update()

pygame.quit()
