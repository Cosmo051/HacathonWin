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
pygame.init()



def draw_static_bg(screen):
    bg_image = pygame.image.load("assets\\backgrounds-assets\cloud.jpg")
    bg_image = pygame.transform.scale(bg_image, (1600, 800))
    screen.blit(bg_image, (0,0))

#font = pygame.font.Font('', 32)
#text = font.render('Connection Quest', True, (255,0,0), False)

screen = pygame.display.set_mode((1600, 800))
while True:
    draw_static_bg(screen)
#screen.blit(text, (100, 300))
