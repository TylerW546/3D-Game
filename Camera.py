import pygame
import math
from AngleCalculations import *

from Vector3 import Vector3

class Camera():
    active_camera = None

    def __init__(self):
        self.position = Vector3(100,100,0)

        self.pitch = 0
        self.yaw = 0

        Camera.active_camera = self

    def draw(self, screen, points):
        for point in points:
            screen_x = None
            screen_y = None
            
            relative_point = point.getDuplicate()
            relative_point.subtract(self.position)

            yaw_angle = angleFromPoints(0, 0, relative_point.x, relative_point.y)
            if angleInRange(yaw_angle-self.yaw+2*math.pi,-math.pi/6, math.pi/6):
                screen_x = 500*angleInRange(yaw_angle-self.yaw+2*math.pi, -math.pi/6, math.pi/6)

            pitch_angle = angleFromPoints(0, 0, Vector3(relative_point.x, relative_point.y, 0).getMagnitude(), relative_point.z)
            if angleInRange(pitch_angle-self.pitch+2*math.pi,-math.pi/6, math.pi/6):
                screen_y = 500*angleInRange(pitch_angle-self.pitch+2*math.pi, -math.pi/6, math.pi/6)
            
            radius = 400/Vector3(relative_point.x, relative_point.y, 0).getMagnitude()

            if screen_x and screen_y:
                pygame.draw.circle(screen, (200,0,0), (screen_x, screen_y), radius)

    def draw2D(self, screen, points):
        pygame.draw.circle(screen, (0,200,0), (self.position.x, self.position.y), 4)
        pygame.draw.lines(screen, (0,0,200), False, [(self.position.x+100*math.cos(self.yaw+math.pi/6), self.position.y+100*math.sin(self.yaw+math.pi/6)), (self.position.x+100*math.cos(self.yaw-math.pi/6), self.position.y+100*math.sin(self.yaw-math.pi/6))])
        pygame.draw.lines(screen, (0,0,200), False, [(self.position.x, self.position.y), (self.position.x+100*math.cos(self.yaw+math.pi/6), self.position.y+100*math.sin(self.yaw+math.pi/6))])
        pygame.draw.lines(screen, (0,0,200), False, [(self.position.x, self.position.y), (self.position.x+100*math.cos(self.yaw-math.pi/6), self.position.y+100*math.sin(self.yaw-math.pi/6))])
        for point in points:
            pygame.draw.circle(screen, (0,200,0), (point.x, point.y), 2)
        
