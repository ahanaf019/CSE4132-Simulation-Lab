import turtle

def draw_bezier_curve(control_points):
    turtle.penup()
    turtle.goto(control_points[0])

    turtle.pendown()
    turtle.color("blue")

    for t in range(0, 101, 5):
        x, y = bezier_point(control_points, t / 100)
        turtle.goto(x, y)
        turtle.dot(5)  # Optional: Draw dots at each point on the curve

    turtle.done()

def bezier_point(control_points, t):
    n = len(control_points) - 1
    x, y = 0, 0

    for i, point in enumerate(control_points):
        coefficient = binomial_coefficient(n, i) * (1 - t)**(n - i) * t**i
        x += coefficient * point[0]
        y += coefficient * point[1]

    return x, y

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

# Example usage:
control_points = [(-100, -50), (0, 100), (100, -50)]
control_points = [
    (20, 80),
    (30, 20),
    (90, 25),
    (85, 60),
]
draw_bezier_curve(control_points)