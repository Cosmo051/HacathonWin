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
from player import *
pygame.joystick.init()
pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 864
BG = (50, 50, 50)
BLACK = (0, 0, 0)
portal_img = pygame.image.load("assets\\backgrounds-assets\portal.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Eternal")
STAGE_FILE = "stage.txt"
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

def read_stage():
    curr_stage = 0
    with open(STAGE_FILE, 'r') as file:
        curr_stage = int(float(file.read()))
    return curr_stage

def write_stage(new_stage):
    with open(STAGE_FILE, 'w') as file:
        file.write(str(new_stage))
# background code---------------------------------------------------------start
# define game variables
scroll = 0
bg_index = 1

def load_ground(index):
    ground_image = pygame.image.load(
        f"assets/backgrounds-assets/_PNG/{index}/1.png"
    ).convert_alpha()
    ground_width = ground_image.get_width()
    ground_height = ground_image.get_height()
    return ground_image, ground_width, ground_height

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
    Platform(plat_img_path, 120, 25, 2000, 150),
    Platform(plat_img_path, 130, 30, 2200, 250),
    Platform(plat_img_path, 100, 20, 2400, 150),
    Platform(plat_img_path, 140, 25, 2600, 350),
    Platform(plat_img_path, 150, 35, 2800, 450),
    Platform(plat_img_path, 120, 30, 3000, 350)
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
    Platform(plat_img_path, 110, 40, 1900, 300),
    Platform(plat_img_path, 120, 30, 2100, 400),
    Platform(plat_img_path, 100, 25, 2300, 500),
    Platform(plat_img_path, 130, 35, 2500, 400),
    Platform(plat_img_path, 140, 30, 2700, 300),
    Platform(plat_img_path, 110, 20, 2900, 200),
    Platform(plat_img_path, 150, 25, 3100, 300)
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
    Platform(plat_img_path, 150, 30, 2000, 250),
    Platform(plat_img_path, 120, 35, 2200, 350),
    Platform(plat_img_path, 130, 20, 2400, 450),
    Platform(plat_img_path, 140, 25, 2600, 350),
    Platform(plat_img_path, 110, 30, 2800, 250),
    Platform(plat_img_path, 100, 20, 3000, 150),
    Platform(plat_img_path, 120, 25, 3200, 250)
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
    Platform(plat_img_path, 130, 35, 1900, 400),
    Platform(plat_img_path, 120, 25, 2100, 500),
    Platform(plat_img_path, 140, 30, 2300, 400),
    Platform(plat_img_path, 150, 20, 2500, 300),
    Platform(plat_img_path, 130, 35, 2700, 200),
    Platform(plat_img_path, 110, 30, 2900, 300),
    Platform(plat_img_path, 120, 20, 3100, 400)
]

def load_bg_images(index):
    bg_images = []
    for i in range(7, 1, -1):
        bg_image = pygame.image.load(
            f"assets/backgrounds-assets/_PNG/{index}/{i}.png"
        ).convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        bg_images.append(bg_image)
    bg_width = bg_images[0].get_width()
    return bg_images, bg_width


def draw_bg(cris_list_dog1, cris_list_cat1, offset, images, width):
    for x in range(5):
        speed = 1
        for i in images:
            screen.blit(i, ((x * width) - offset * speed, 0))
            speed += 0.2
            # drawing platforms
    portal = pygame.transform.scale(portal_img, (300, 300))
    screen.blit(portal, (2500 - offset, 334))
    draw_platforms(plat_lst_1, screen, offset)
    draw_crystals(screen, cris_list_dog1, offset)
    draw_crystals(screen, cris_list_cat1, offset)


def draw_ground(offset, image, width, height):
    for x in range(15):
        screen.blit(
            image,
            ((x * width) - offset * 2.5, SCREEN_HEIGHT - height),
        )


def draw_platforms(platform_lst: list, screen, offset):
    pass


# background code---------------------------------------------------------------------end


# position helper func
def read_pos(str:str):
    if str == "reset":
        return "reset"
    str = str.split("_")
    return int(str[0]), int(str[1]), str[2], eval(str[3]), int(str[4])

def make_pos(tup):
    if tup == "reset":
        return "reset"
    return str(tup[0]) + "_" + str(tup[1]) + "_" + str(tup[2]) + "_" + str(tup[3]) + "_" + str(tup[4])


def redrawWindow(window, dog, cat, dog_state, cat_state, index,portal):
    dog.draw(window, dog_state, index)
    cat.draw(window, cat_state, index)
    portal = pygame.transform.scale(portal, (300, 300))
    screen.blit(portal, (2500, 634))
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
scroll = start_pos[4]
dog_x = 0
cat_x = 0

dog_y = 634
cat_y = 634


dog = Player(start_pos[0], start_pos[1], 48, 48, "dog")
cat = Player(0, 0, 48, 48, "cat")
dog_img = dog.get_frames_dic()[state_dog][0]
cat_img = cat.get_frames_dic()["Idle"][0]
jumping = False


def gravitational_force(player: Player, flag1, plat1):
    dog.update()
    jumping = False
    if (not flag1) and (player.get_y() < GROUND_LEVEL):
        if player.y + GRAVITY > GROUND_LEVEL:
            player.y = GROUND_LEVEL
        else:
            player.y = player.y + GRAVITY
    elif flag1:
        player.y = plat1.y - player.height - plat1.height


def reset_game():
    n.send("reset")

def create_crystals(coor):
    cris_list_created = []
    for i in range(len(coor[0])):
        cris_list_created.append(Cristal(coor[0][i], coor[1][i], CRIS_WIDTH, CRIS_HEIGHT, "assets\cristal assets\PNG\shiny\\4.png", "dog"))
    return cris_list_created

def draw_crystals(screen, cris_list, offset):
    for cris in cris_list:
        cris.draw(screen, offset)

def move_crystals(cris_list):
    for cris in cris_list:
        cris.move()

def collect_crystal(cris_list, cris_cord_list):
    for i in range(len(cris_list)):
        if (cris_list[i].get_X() > dog.x and cris_list[i].get_X() < dog.x + dog.width) and (cris_list[i].get_y() > dog.y and cris_list[i].get_y() < dog.y + dog.height):
            cris_list[i].is_collected = True
            cris_cord_list[0].remove(cris_cord_list[0][i])
            cris_cord_list[1].remove(cris_cord_list[1][i])

def end_game():
    pass


def plat_collision_check(player, lst):
    pass

stage = read_stage()
plat_lst = []
joysticks = []
move_left = False
move_right = False
cris_list_dog = create_crystals(cris_list_cord)
cris_flag = True
finish = False

bg_images, bg_width = load_bg_images(stage)
ground_image, ground_width, ground_height = load_ground(stage)
while run:
    clock.tick(10)
    # update background
    screen.fill(BG)

    cat_pos = read_pos(n.send(make_pos((dog.x, dog.y, state_dog, cris_list_cord, scroll))))
    cat.x = cat_pos[0]
    cat.y = cat_pos[1]
    state_cat = cat_pos[2]
    scroll_cat = cat_pos[4]
    cris_list_cat = create_crystals(cat_pos[3])

    cat.update()
    # draw world
    draw_bg(cris_list_dog, cris_list_cat, combined_offset, bg_images, bg_width)
    draw_ground(combined_offset, ground_image, ground_width, ground_height)
    
    key = pygame.key.get_pressed()
    # state handling----------------
    if len(joysticks) == 0:
        if key[pygame.K_d]:
            state_dog = "Walk"
            if dog.x < WALKING_LIMIT:
                dog.x += dog.horiz_speed
        elif key[pygame.K_a]:
            state_dog = "WalkBack"
            if dog.x >= 0:
                dog.x -= dog.horiz_speed
        elif key[pygame.K_e]:
            finish = True
        else:
            state_dog = "Idle"
        
        if (
        cat.get_x() > SCREEN_WIDTH / 2
        and dog.get_x() > SCREEN_WIDTH / 2
        and key[pygame.K_d]
        ):
            scroll += 5

        if (
        cat.get_x() < SCREEN_WIDTH / 2
        and dog.get_x() < SCREEN_WIDTH / 2
        and key[pygame.K_a]
        ):
            scroll -= 5
    else:
        for joystick in joysticks:
            if joystick.get_button(0):
                jumping = True
            
            #player movement with stick
            horiz_move = joystick.get_axis(0)
            if horiz_move > 0.05:
                state_dog = "Walk"
            elif horiz_move < -0.05:
                state_dog = "WalkBack"
            else:
                state_dog = "Idle"
            
            if state_dog != "idle" and (0 <= dog.x <= WALKING_LIMIT):
                dog.x += int(dog.horiz_speed * horiz_move)
            
            if(cat.get_x() > SCREEN_WIDTH / 2 and dog.get_x() > SCREEN_WIDTH / 2 and horiz_move > 0.05):
                scroll += 5
            if(cat.get_x() < SCREEN_WIDTH / 2 and dog.get_x() < SCREEN_WIDTH / 2 and horiz_move < -0.05):
                scroll -= 0.05
    
    if key[pygame.K_SPACE]:
        jumping = True
    
    if jumping:
        dog.y -= dog.y_velocity
        dog.y_velocity -= dog.y_gravity
        dog.update()
        if dog.jump_height < -dog.y_velocity:
            dog.y_velocity = dog.jump_height
            jumping = False
        dog.update()

    # show frame image
    i += 1
    if i >= len(dog.get_frames_dic()["Idle"]):
        i = 0

    #create_crystals(screen, cris_list_dog)
    move_crystals(cris_list_dog)
    # Yaniv stuff
    if (not jumping):
        gravitational_force(dog, flag, plat)
        dog.update()
    
    if finish:
        if stage < 4:
            stage += 1
            write_stage(stage)
            dog.x = 0
            dog.y = 634
            finish = False
            match stage:
                case 1:
                    bg_index = 3
                    plat_lst = plat_lst_1
                case 2:
                    bg_index = 2
                    plat_lst = plat_lst_2
                case 3:
                    bg_index = 4
                    plat_lst = plat_lst_3
                case 4:
                    bg_index = 1
                    plat_lst = plat_lst_4
            bg_images, bg_width = load_bg_images(stage)
            ground_image, ground_width, ground_height = load_ground(stage)
        else:
            end_game()
        
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
        if event.type == pygame.QUIT:
            run = False
    dog.update()
    # collect_crystal(cris_list_dog, cris_list_cord)
    redrawWindow(screen, dog, cat, state_dog, state_cat, i, portal_img)
    # pygame.display.update()

pygame.quit()
