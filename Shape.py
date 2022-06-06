from Line import Line

class Triangle:
    def __init__(self, points):
        self.lines = [Line(points[-1+i], points[i]) for i in range(3)]