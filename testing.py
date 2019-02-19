from graphics import *
from math import *

class Velocity:
    def __init__(self, magnitude, direction):
        self.magnitude = magnitude
        self.direction = direction
a1 = Velocity (1, 4)

class Vector2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def direction(self):
        return degrees(atan(self.y / self.x))

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)
def sim():
    win = GraphWin("ArterySim", 1000, 700)
    a1 = Point(300,500)
    a1.draw(win)
    a2 = Point(300,200)
    a2.draw(win)
    b = Point(600, 100)
    b.draw(win)
    circ1 = Circle(a1, 150)
    circ1.draw(win)
    circ2 = Circle(a2,150)
    circ2.draw(win)

    for i in range(300):
        a1.move(1,-1)
        circ1.move(1,-1)
        a2.move(1,-0)
        circ2.move(1,0)
        time.sleep(0.01)


        if (a1.x - b.x) ** 2 + (a1.y - b.y) ** 2 <= circ1.radius ** 2:
            vector_a1_b = b.x * b.y - a1.x * a1.y
            a1.velocity = normalized(vector_a1_b) * vector_a1_b.velocity.magnitude

        a1.x += a1.velocity.x
        a1.y += a1.velocity.y

    win.getMouse()
    win.close()
sim()
