import math

def angleFromPoints(x1, y1, x2, y2):
    x_diff = x2-x1
    y_diff = y2-y1

    return math.atan2(y_diff, x_diff)

def angleInRange(angle, a1, a2):
    while angle < 0:
        angle += 2*math.pi
    angle %=(2*math.pi)
    
    range = a2-a1
    
    if (angle > a1 and angle < a2):
        return (angle-a1)/range
    elif (angle-2*math.pi > a1 and angle-2*math.pi < a2) :
        return (angle-2*math.pi-a1)/range
    elif (angle+2*math.pi > a1 and angle+2*math.pi < a2) :
        return (angle-a1)/range
    else:
        return False