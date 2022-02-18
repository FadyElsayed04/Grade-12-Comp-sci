from graphics import * 

def cantor(win, x1, x2, y):
    pt = Point(x1, y)
    pt1 = Point(x2, y)
    li = Line(pt, pt1)
    li.draw(win)

    pt = Point(x1, y + 20)
    pt1 = Point(x2 // 3, y + 20)
    li = Line(pt, pt1)
    li.draw(win)

    pt = Point(x2, y + 20)
    pt1 = Point(x2 - (x2 - x1) // 3, y + 20)
    li = Line(pt, pt1)
    li.draw(win)


def main():
    win = GraphWin("Cantor Set", 300, 200)
    win.setCoords(0, 0, 300, 200)
    cantor(win, 10, 290, 10)
    win.getMouse()
    win.close()

main()
