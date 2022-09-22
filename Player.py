from Camera import Camera
from Vector3 import Vector3

import math

class Player():
    def __init__(self, position):
        self.position = position
        self.camera = Camera()

        self.pitch = 0
        self.yaw = 0

    def move(self, keys_pressed):
        pass

    def turn(self, mouse_movement_since_last_frame):
        self.yaw = (self.yaw + mouse_movement_since_last_frame[0]/250) % (math.pi*2)
        self.pitch = (self.pitch + mouse_movement_since_last_frame[1]/250) % (math.pi*2)
        self.camera.yaw = self.yaw
        self.camera.pitch = self.pitch

