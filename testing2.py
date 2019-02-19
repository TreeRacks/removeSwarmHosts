from graphics import *
from threading import Timer


def main():

    win = GraphWin("AnimationTest", 500,500)
    b = Point(400, 100)
    b.draw(win)



    a = Point(100, 200)
    a.draw(win)


    circ = Circle(a, 150)
    circ.draw(win)

    for i in range(190):
        a.move(1, 0)
        circ.move(1,0)
        time.sleep(0.01)

    time.sleep(1.0)
    for i in range(99):
        a.move(1.1, -1)
        circ.move(1, -1)
        time.sleep(0.01)


    win.getMouse()
    win.close()



main()

