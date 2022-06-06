import math

def angleFromPoints(x1, y1, x2, y2):
    x_diff = x2-x1
    y_diff = y2-y1

    if x_diff == 0:
        if y_diff > 0:
            return math.pi/2
        else:
            return math.pi*3/2
    elif y_diff == 0:
        if x_diff > 0:
            return 0
        else:
            return math.pi/2
    else:
        if x_diff > 0:
            return (math.atan(y_diff/x_diff) + math.pi*2) % (math.pi*2)
        else:
            return (math.atan(y_diff/x_diff) + math.pi*3) % (math.pi*2)

def angleInRange(angle, a1, a2):
    range = a2-a1
    
    if (angle > a1 and angle < a2):
        return (angle-a1)/range
    elif (angle-2*math.pi > a1 and angle-2*math.pi < a2) :
        return (angle-2*math.pi-a1)/range
    elif (angle+2*math.pi > a1 and angle+2*math.pi < a2) :
        return (angle-a1)/range
    else:
        return False