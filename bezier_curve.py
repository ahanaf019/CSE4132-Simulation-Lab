import turtle
import math
import time

def nCk(n, k):
    sum = 1
    for i in range(1, k+1):
        sum = sum * (n - k + i) / i
    return int(sum)


def BEZ(u, n, k):
    return nCk(n, k) * math.pow(u, k) * math.pow(1 - u, n - k)
    
    
def bezier_curve(points):
    u = 0
    du = 0.001
    n = len(points) - 1
    
    while u < 1:
        px = 0
        py = 0
        for k, point in enumerate(points):
            coeff = BEZ(u, n, k)
            px += point[0] * coeff
            py += point[1] * coeff
            
        # turtle.penup()
        turtle.goto((px, py))
        turtle.dot(size=2)
        # turtle.penup()
            
            
        
        u += du
    turtle.done()
def plot_points(points):
    for point in points:
        turtle.penup()
        turtle.goto((point[0], point[1]))
        turtle.dot(size=10)
        turtle.penup()
        time.sleep(1)

turtle.hideturtle()
turtle.speed(0)


points = [
    (-200, 180),
    (300, 200),
    (-100, 250),
    (250, 400),
]
plot_points(points)
bezier_curve(points)
# turtle.penup()
# turtle.goto(10, 10)
# turtle.dot()
# time.sleep(1)