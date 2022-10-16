from pygame import Vector3

class Plane():
    all_planes = []
    rendered_planes = []
        
    def __init__(self, points, render=False, color = (255,0,0)):
        self.points = points
        self.render = render
        self.color = color
        
        Plane.all_planes.append(self)
        if self.render:
            Plane.rendered_planes.append(self)