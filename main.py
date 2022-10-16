import imp
import math
import random
import time

import pygame
from pygame.locals import *

from Vector3 import Vector3
from Camera import Camera
from Point import Point
from Line import Line
from Plane import Plane
from Player import Player

from config import *

pygame.font.init()
default_font = pygame.font.SysFont('Times New Roman', 20)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("3D Game Engine (WIP)")

points = [[Point(Vector3(10*x, 10*y, math.pi/10*x),render=True) for x in range(-10,11)] for y in range(-10,11)] 
planes = [Plane((points[x][y], points[x+1][y], points[x+1][y+1], points[x][y+1]), render=True, color = [random.randrange(0,255) for i in range(3)]) for x in range(20) for y in range(20)]

player = Player(Vector3())
player.camera.yaw = math.pi/2

pygame.mouse.set_pos([SCREEN_WIDTH/2,SCREEN_HEIGHT/2])
pygame.mouse.get_rel()
pygame.mouse.set_visible(False)
def main():
    i = 1
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                player.turn(pygame.mouse.get_rel())
                pygame.mouse.set_pos([SCREEN_WIDTH/2,SCREEN_HEIGHT/2])
                pygame.mouse.get_rel()

        screen.fill(background)
        
        player.move(pygame.key.get_pressed())
        
        player.camera.drawFixedMiniMap(screen, Point.rendered_points)
        
        player.camera.drawPoints(screen, Point.rendered_points)
        player.camera.drawLines(screen, Line.rendered_lines)
        player.camera.drawPlanes(screen, Plane.rendered_planes)

        for list in points:
            for point in list:
                point.position = point.initial_position.getDuplicate()
                point.position.z = math.sin(point.position.z+i)*45-80
        i += math.pi/50
        i %= 2*math.pi
        
        pygame.display.update()
        
        time.sleep(.01)

if __name__ == "__main__":
    main()