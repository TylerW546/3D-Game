import pygame
import math
from AngleCalculations import *

from Vector3 import Vector3

class Camera():
    active_camera = None

    def __init__(self):
        self.position = Vector3()

        self.pitch = 0
        self.yaw = 0

        Camera.active_camera = self

    def draw(self, screen, points):
        for point in points:
            screen_x = None
            screen_y = 250
            
            relative_point = point.getDuplicate()
            relative_point.subtract(self.position)

            yaw_angle = angleFromPoints(0,0, relative_point.x, relative_point.y)
            
            if angleInRange(yaw_angle-self.yaw, -math.pi/6, math.pi/6):
                screen_x = 500*angleInRange(yaw_angle-self.yaw, -math.pi/6, math.pi/6)
            
            if screen_x and screen_y:
                pygame.draw.circle(screen, (200,0,0), (screen_x, screen_y), 2)
        
        self.yaw = (self.yaw + math.pi/1028) % (math.pi*2)


