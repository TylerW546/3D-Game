import pygame
import math
from AngleCalculations import *

from Vector3 import Vector3

from config import *

class Camera():
    active_camera = None

    def __init__(self):
        self.position = Vector3(100,100,0)

        self.pitch = 0
        self.yaw = 0

        Camera.active_camera = self

    def drawPoints(self, screen, points):
        for point in points:
            screen_x = None
            screen_y = None
            
            relative_point = point.position.getDuplicate()
            relative_point.subtract(self.position)

            yaw_angle = angleFromPoints(0, 0, relative_point.x, relative_point.y)
            if angleInRange(yaw_angle-self.yaw,-math.pi/6, math.pi/6):
                screen_x = SCREEN_WIDTH*angleInRange(yaw_angle-self.yaw, -math.pi/6, math.pi/6)

            pitch_angle = angleFromPoints(0, 0, relative_point.z, Vector3(relative_point.x, relative_point.y, 0).getMagnitude())
            if angleInRange(pitch_angle-self.pitch,-math.pi/6, math.pi/6):
                screen_y = SCREEN_HEIGHT*angleInRange(pitch_angle-self.pitch, -math.pi/6, math.pi/6)
            
            if (Vector3(relative_point.x, relative_point.y, relative_point.z).getMagnitude() > 1):
                radius = 800/Vector3(relative_point.x, relative_point.y, relative_point.z).getMagnitude()
            else:
                radius = 800

            if screen_x and screen_y:
                pygame.draw.circle(screen, (200,0,0), (screen_x, screen_y), radius)

    def drawLines(self, screen, lines):
        for line in lines:
            screen_x_list = []
            screen_y_list = []
            sides = []
            for point in line.points:
                relative_point = point.position.getDuplicate()
                relative_point.subtract(self.position)

                yaw_angle = angleFromPoints(0, 0, relative_point.x, relative_point.y)
                screen_x = SCREEN_WIDTH*angleInRange(yaw_angle-self.yaw, -math.pi/6, math.pi/6)

                pitch_angle = angleFromPoints(0, 0, relative_point.z, Vector3(relative_point.x, relative_point.y, 0).getMagnitude())
                screen_y = SCREEN_HEIGHT*angleInRange(pitch_angle-self.pitch, -math.pi/6, math.pi/6)
                
                side = None
                pos = Vector3(screen_x, screen_y)
                if screen_x < 0:
                    pos = Vector3(screen_x, screen_y).scalarMultiply(SCREEN_WIDTH/(SCREEN_WIDTH-screen_x))
                    side = "left"
                elif screen_x > SCREEN_WIDTH:
                    pos = Vector3(screen_x, screen_y).scalarMultiply(SCREEN_WIDTH/(screen_x-SCREEN_WIDTH))
                    side = "right"
                    
                if screen_y < 0:
                    pos = Vector3(screen_x, screen_y).scalarMultiply(SCREEN_HEIGHT/(SCREEN_HEIGHT-screen_x))
                    side = "top"
                elif screen_y > SCREEN_HEIGHT:
                    pos = Vector3(screen_x, screen_y).scalarMultiply(SCREEN_HEIGHT/(screen_x-SCREEN_HEIGHT))
                    side = "bottom"
                    
                screen_x_list.append(pos.x)
                screen_y_list.append(pos.y)
                sides.append(side)
            
            if None in sides or sides[0] != sides[1]:
                pygame.draw.lines(screen, (line.color), False, ((screen_x_list[0], screen_y_list[0]), (screen_x_list[1], screen_y_list[1])))
    
    def drawPlanes(self, screen, planes):
        for plane in planes:
            screen_x_list = []
            screen_y_list = []
            sides = []
            for point in plane.points:
                relative_point = point.position.getDuplicate()
                relative_point.subtract(self.position)

                yaw_angle = angleFromPoints(0, 0, relative_point.x, relative_point.y)
                screen_x = SCREEN_WIDTH*angleInRange(yaw_angle-self.yaw, -math.pi/6, math.pi/6)

                pitch_angle = angleFromPoints(0, 0, relative_point.z, Vector3(relative_point.x, relative_point.y, 0).getMagnitude())
                screen_y = SCREEN_HEIGHT*angleInRange(pitch_angle-self.pitch, -math.pi/6, math.pi/6)
                
                side = None
                pos = Vector3(screen_x, screen_y)
                if screen_x < 0:
                    pos = Vector3(screen_x, screen_y).scalarMultiply(SCREEN_WIDTH/(SCREEN_WIDTH-screen_x))
                    side = "left"
                elif screen_x > SCREEN_WIDTH:
                    pos = Vector3(screen_x, screen_y).scalarMultiply(SCREEN_WIDTH/(screen_x-SCREEN_WIDTH))
                    side = "right"
                    
                if screen_y < 0:
                    pos = Vector3(screen_x, screen_y).scalarMultiply(SCREEN_HEIGHT/(SCREEN_HEIGHT-screen_x))
                    side = "top"
                elif screen_y > SCREEN_HEIGHT:
                    pos = Vector3(screen_x, screen_y).scalarMultiply(SCREEN_HEIGHT/(screen_x-SCREEN_HEIGHT))
                    side = "bottom"
                    
                screen_x_list.append(pos.x)
                screen_y_list.append(pos.y)
                sides.append(side)
            
            polylist = [(screen_x_list[i],screen_y_list[i]) for i in range(len(screen_x_list))]
            pygame.draw.polygon(screen, (plane.color), polylist)
                
                
                

    def drawFixedMiniMap(self, screen, points):
        minimap = pygame.Surface((mini_w,mini_h))
        minimap.fill(mini_background)
        
        pygame.draw.circle(minimap, (0,200,0), (self.position.x*mini_w/mini_w_coverage+mini_w/2, self.position.y*mini_h/mini_h_coverage+mini_h/2), 4)
        pygame.draw.lines(minimap, (0,0,200), False, [(self.position.x*mini_w/mini_w_coverage+mini_w/2+100*math.cos(self.yaw+math.pi/6), self.position.y*mini_h/mini_h_coverage+mini_h/2+100*math.sin(self.yaw+math.pi/6)), (self.position.x*mini_w/mini_w_coverage+mini_w/2+100*math.cos(self.yaw-math.pi/6), self.position.y*mini_h/mini_h_coverage+mini_h/2+100*math.sin(self.yaw-math.pi/6))])
        pygame.draw.lines(minimap, (0,0,200), False, [(self.position.x*mini_w/mini_w_coverage+mini_w/2, self.position.y*mini_h/mini_h_coverage+mini_h/2), (self.position.x*mini_w/mini_w_coverage+mini_w/2+100*math.cos(self.yaw+math.pi/6), self.position.y*mini_h/mini_h_coverage+mini_h/2+100*math.sin(self.yaw+math.pi/6))])
        pygame.draw.lines(minimap, (0,0,200), False, [(self.position.x*mini_w/mini_w_coverage+mini_w/2, self.position.y*mini_h/mini_h_coverage+mini_h/2), (self.position.x*mini_w/mini_w_coverage+mini_w/2+100*math.cos(self.yaw-math.pi/6), self.position.y*mini_h/mini_h_coverage+mini_h/2+100*math.sin(self.yaw-math.pi/6))])
        for point in points:
            pygame.draw.circle(minimap, (0,200,0), (point.position.x*mini_w/mini_w_coverage+mini_w/2, point.position.y*mini_h/mini_h_coverage+mini_h/2), 2)
            
        screen.blit(minimap, (0,0))
        
