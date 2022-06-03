import math
import random
import time

import pygame
from pygame.locals import *

from Vector3 import Vector3
from Camera import Camera

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
settingsColor = (100,100,200)

white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
blue = (0, 0, 255)
background = black

pygame.font.init()
defaultFont = pygame.font.SysFont('Times New Roman', 20)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF, 32)

points = [Vector3(10*i, 0, 0) for i in range(10)] 
Camera()

def main():
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(background)

        
        Camera.active_camera.draw(screen, points)

        pygame.display.update()
        
        time.sleep(.001)

if __name__ == "__main__":
    main()