from graphics import *
import math


def tree(win, x, y, length, theta):
    if length <= 2.5:
        return
    
    x2 = x - (length * math.cos(theta))
    y2 = y - (length * math.sin(theta))
    
    pt = Point(x, y)
    pt2 = Point(x2, y2)
    
    line = Line (pt, pt2)
    line.draw(win)
    
    tree(win, x2, y2, length * 0.675, theta + (math.pi / 6))
    tree(win, x2, y2, length * 0.675, theta - (math.pi / 6))
    

def main():
    win = GraphWin("Tree", 500, 500)
    win.setCoords(500, 500, 0, 0)
    
    tree(win, 250, 500, 150, math.pi / 2)
    
    win.getMouse()
    win.close()


main()
