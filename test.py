
from graphics import *

def main():
    win = GraphWin("My Graphics Winder", 400, 400)

    c = Circle(Point(50,50), 10)
    c.draw(win)
    for i in range(2500):
            c.move(0.1,0)
            time.sleep(0.001)

    win.getMouse()
    win.close()

main()