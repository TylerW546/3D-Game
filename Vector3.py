import math

class Vector3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def getDuplicate(self):
        return Vector3(self.x, self.y, self.z)

    def getMagnitude(self):
        return math.dist((0,0,0), (self.x, self.y, self.z))

    def setMagnitude(self, mag):
        self.scalarMultiply(mag/self.getMagnitude())
    
    def scalarMultiply(self, mult):
        self.x*=mult
        self.y*=mult
        self.z*=mult

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def dotProduct(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z

    def decomposeTo(self, other):
        dot_prod = self.dotProduct(other)

        v_p = None
        if other.getMagnitude() != 0:
            v_p = other.getDuplicate()
            v_p.scalarMultiply(dot_prod/other.getMagnitude()/other.getMagnitude())
        else:
            v_p = Vector3()
        v_o = self.getDuplicate()
        v_o.subtract(v_p)

        return v_p, v_o

    def angleTo(self, other):
        dot_prod = self.dotProduct(other)

        return math.acos(dot_prod/self.getMagnitude()/other.getMagnitude())

    def __str__(self):
        return "X: " + str(self.x) + "  Y: " + str(self.y) + "  Z: " + str(self.z)