from graphics import * 
import math

def koch(win, x1, y1, x2, y2) :
    pt = Point(x1, y1)
    pt1 = Point(x2, y2)
    line = Line(pt, pt1)
    line.draw(win)

    length = (x2 - x1) / 3
    base = length / 2
    height = math.sqrt((length ** 2) - (base ** 2))
    
    
    pt = Point(150, y2 + height)
    pt1 = Point(x2 - length, y2)
    line = Line(pt, pt1)
    line.draw(win)

    pt = Point(150, y1 + height)
    pt1 = Point(x1 + length, y2)
    line = Line(pt, pt1)
    line.draw(win)   

    pt = Point(x1 + length + 1, y1)
    pt1 = Point(x2 - length, y2)
    line = Line(pt, pt1)
    line.draw(win)
    line.setFill("white")

    
def main():
    win = GraphWin("Koch Snowflake", 300, 400)
    win.setBackground("white")
    win.setCoords(0, 0, 300, 400)
    koch(win, 20, 280, 280, 280) 
    win.getMouse()
    win.close()

main()
