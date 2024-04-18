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
    Platform(plat_img_path, 80, 20, 200, 50),
    Platform(plat_img_path, 70, 15, 400, 150),
    Platform(plat_img_path, 60, 25, 600, 250),
    Platform(plat_img_path, 50, 20, 800, 350),
    Platform(plat_img_path, 40, 20, 1000, 450),
    Platform(plat_img_path, 50, 25, 1200, 550),
    Platform(plat_img_path, 60, 20, 1400, 450),
    Platform(plat_img_path, 70, 15, 1600, 350)
]

# List 2
plat_lst_2 = [
    Platform(plat_img_path, 70, 20, 100, 200),
    Platform(plat_img_path, 60, 15, 300, 300),
    Platform(plat_img_path, 50, 25, 500, 400),
    Platform(plat_img_path, 40, 20, 700, 500),
    Platform(plat_img_path, 50, 25, 900, 400),
    Platform(plat_img_path, 60, 15, 1100, 300),
    Platform(plat_img_path, 70, 20, 1300, 200),
    Platform(plat_img_path, 80, 25, 1500, 100)
]

# List 3
plat_lst_3 = [
    Platform(plat_img_path, 50, 20, 200, 350),
    Platform(plat_img_path, 40, 15, 400, 250),
    Platform(plat_img_path, 60, 25, 600, 150),
    Platform(plat_img_path, 70, 20, 800, 250),
    Platform(plat_img_path, 50, 25, 1000, 350),
    Platform(plat_img_path, 40, 15, 1200, 450),
    Platform(plat_img_path, 60, 20, 1400, 350),
    Platform(plat_img_path, 70, 25, 1600, 250)
]

# List 4
plat_lst_4 = [
    Platform(plat_img_path, 60, 20, 100, 500),
    Platform(plat_img_path, 50, 15, 300, 400),
    Platform(plat_img_path, 70, 25, 500, 300),
    Platform(plat_img_path, 40, 20, 700, 200),
    Platform(plat_img_path, 50, 25, 900, 300),
    Platform(plat_img_path, 60, 15, 1100, 400),
    Platform(plat_img_path, 70, 20, 1300, 500),
    Platform(plat_img_path, 80, 25, 1500, 400)
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


def draw_bg(offset, images, width):
    for x in range(5):
        speed = 1
        for i in images:
            screen.blit(i, ((x * width) - offset * speed, 0))
            speed += 0.2
            # drawing platforms
    portal = pygame.transform.scale(portal_img, (portal_width, portal_height))
    screen.blit(portal, (portal_x, 300))


def draw_ground(offset, image, width, height):
    for x in range(15):
        screen.blit(
            image,
            ((x * width) - offset * 2.5, SCREEN_HEIGHT - height),
        )




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


def gravitational_force(player: Player):
    dog.update()
    jumping = False
    if (player.get_y() < GROUND_LEVEL):
        if player.y + GRAVITY > GROUND_LEVEL:
            player.y = GROUND_LEVEL
        else:
            player.y = player.y + GRAVITY


def reset_game():
    n.send("reset")

def create_crystals(coor, type): #type is "dog" or "cat"
    cris_list_created = []
    for i in range(len(coor[0])):
        cris_list_created.append(Cristal(coor[0][i], coor[1][i], CRIS_WIDTH, CRIS_HEIGHT, type))
    return cris_list_created

def draw_crystals(screen, cris_list):
    for cris in cris_list:
        cris.draw(screen)

def move_crystals(cris_list):
    for cris in cris_list:
        cris.move()

def collect_crystal(cris_list, cris_cord_list):
    for i in range(len(cris_list)):
        if (cris_list[i].get_X() > dog.x and cris_list[i].get_X() < dog.x + dog.width) and (cris_list[i].get_y() > dog.y and cris_list[i].get_y() < dog.y + dog.height) and not cris_list[i].is_collected:
            cris_list[i].is_collected = True
            print(i)
            print(cris_cord_list[0][i])
            cris_cord_list[0].remove(cris_cord_list[0][i])
            cris_cord_list[1].remove(cris_cord_list[1][i])
            cris_list.remove(cris_list[i])


portal_width = 600
portal_height = 600
portal_x = 500
portal_y = 634

def draw_platform(plat_lst):
    for plat in plat_lst:
        plat.draw(screen)

def on_portal(dog:Player, cat:Player, scroll):
    portal_rect = pygame.rect.Rect(portal_x, portal_y, portal_width, portal_height)
    if portal_rect.colliderect(dog.get_rect()) or portal_rect.colliderect(cat.get_rect()):
        return True
    return False

def end_game():
    pass

def start_stage(plats):
    pass
def plat_collision_check(player, lst):
    pass
stage = read_stage()
plat_lst = []
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

joysticks = []
move_left = False
move_right = False
cris_list_dog = create_crystals(cris_list_cord, "dog")
cris_flag = True
finish = False
cris_collected_counter = 0
started = False
horiz_move = 0
def plat_collision_check(player, plat_list):
    for plat in plat_list:
        if plat.rect.colliderect(player.rect):
            return True, plat
    return False, None



bg_images, bg_width = load_bg_images(stage)
ground_image, ground_width, ground_height = load_ground(stage)

def draw_static_bg(screen):
    bg_image = pygame.image.load(
            f"assets/backgrounds-assets/_PNG/{bg_index}/background.png"
        )
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(bg_image, (0,0))

while run:
    clock.tick(10)
    # update background
    screen.fill(BG)

    cat_pos = read_pos(n.send(make_pos((dog.x, dog.y, state_dog, cris_list_cord, scroll))))
    cat.x = cat_pos[0]
    cat.y = cat_pos[1]
    state_cat = cat_pos[2]
    scroll_cat = cat_pos[4]
    cris_list_cat = create_crystals(cat_pos[3], "cat")
    cat.update()
    combined_offset = (scroll + scroll_cat)//2
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
        if key[pygame.K_SPACE]:
            jumping = True
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
            
            if (0 <= dog.x <= WALKING_LIMIT):
                dog.x += int(dog.horiz_speed * horiz_move)


    
    
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
    
    # Yaniv stuff
    if (not jumping):
        gravitational_force(dog)
        dog.update()
    
    if on_portal(dog, cat, combined_offset) and (not started):
        started = True
        dog.x = 0
    
    if started:
        draw_static_bg(screen)
        draw_platform(plat_lst)
        draw_crystals(screen, cris_list_dog)
        draw_crystals(screen, cris_list_cat)
        move_crystals(cris_list_dog)
        collect_crystal(cris_list_dog, cris_list_cord)

        flag, plat = plat_collision_check(dog, plat_lst)
        if flag:
            dog.y = plat.y - plat.height - dog.height
        
        if dog.y <= 0 and cat.y <= 0:
            started = False
            finish = True
    else:
        if(cat.get_x() > SCREEN_WIDTH / 2 and dog.get_x() > SCREEN_WIDTH / 2 and horiz_move > 0.05):
            scroll += 5
        if(cat.get_x() < SCREEN_WIDTH / 2 and dog.get_x() < SCREEN_WIDTH / 2 and horiz_move < -0.05):
            scroll -= 5
        
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
        
        combined_offset = (scroll + scroll_cat)//2
        draw_bg(combined_offset, bg_images, bg_width)
        draw_ground(combined_offset, ground_image, ground_width, ground_height)
    
    print(str(pygame.joystick.get_count()))
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
    redrawWindow(screen, dog, cat, state_dog, state_cat, i, portal_img)
    # pygame.display.update()

pygame.quit()
