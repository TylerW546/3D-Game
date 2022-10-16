from pygame import Vector3

class Line():
    all_lines = []
    rendered_lines = []
        
    def __init__(self, p1, p2, render=False, color = (255,0,0)):
        self.points = [p1, p2]
        self.render = render
        self.color = color
        
        Line.all_lines.append(self)
        if self.render:
            Line.rendered_lines.append(self)