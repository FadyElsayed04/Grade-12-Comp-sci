from graphics import * 

def circle(win, x, y, radius):
    pt = Point(x, y)
    circ = Circle(pt, radius)
    circ.draw(win)

    pt = Point(x + 80, y)
    circ = Circle(pt, radius // 2)
    circ.draw(win)

    pt = Point(x - 80, y)
    circ = Circle(pt, radius // 2)
    circ.draw(win)

def main():
    win = GraphWin("Circle", 300, 400)
    win.setCoords(0, 0, 300, 400)
    circle(win, 150, 200, 80)
    win.getMouse()
    win.close()

main()
