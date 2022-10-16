from Camera import Camera
from Vector3 import Vector3
import pygame

import math

class Player():
    def __init__(self, position):
        self.position = position
        self.camera = Camera()

        self.pitch = 0
        self.yaw = 0
        
        self.speed = 5

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.position.x += math.cos(self.yaw) * self.speed
            self.position.y += math.sin(self.yaw) * self.speed
        if keys_pressed[pygame.K_a]:
            self.position.x += math.cos(self.yaw-math.pi/2) * self.speed
            self.position.y += math.sin(self.yaw-math.pi/2) * self.speed
        if keys_pressed[pygame.K_s]:
            self.position.x += math.cos(self.yaw+math.pi) * self.speed
            self.position.y += math.sin(self.yaw+math.pi) * self.speed
        if keys_pressed[pygame.K_d]:
            self.position.x += math.cos(self.yaw+math.pi/2) * self.speed
            self.position.y += math.sin(self.yaw+math.pi/2) * self.speed

    def turn(self, mouse_movement_since_last_frame):
        self.camera.position = self.position
        self.yaw = (self.yaw + mouse_movement_since_last_frame[0]/250) % (math.pi*2)
        self.pitch = (self.pitch + mouse_movement_since_last_frame[1]/250) % (math.pi*2)
        self.camera.yaw = self.yaw
        self.camera.pitch = self.pitch

