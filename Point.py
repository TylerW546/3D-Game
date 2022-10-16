from Vector3 import Vector3


class Point():
    all_points = []
    rendered_points = []
    
    def  __init__(self, position = Vector3(), render = False, color = [255,0,0]):
        self.initial_position = position
        self.position = position
        self.rendered = render
        
        Point.all_points.append(self)
        if self.rendered:
            Point.rendered_points.append(self)
    
        