import pygame
from pygame import *

import time
import sys

shouldPlay= True
pygame.init()
screen=pygame.display.set_mode((400,400),0,32)
pygame.mixer.init()
hornSound= pygame.mixer.Sound("horns.wav")

def start():
    shouldPlay = True
    playSound()

def playSound():
    hornSound.play()

start()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
                 sys.exit()
            if event.key==K_KP2:
                playSound()
    pygame.display.update()
