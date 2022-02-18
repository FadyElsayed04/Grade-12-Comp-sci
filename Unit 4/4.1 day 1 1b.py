from graphics import * 

win = GraphWin("Balloons", 200, 300)
win.setCoords(0, 0, 200, 300)

pt = Point(150, 215)
pt2 = Point(100, 50)
line = Line(pt, pt2)
line.draw(win)

pt = Point(50, 200)
pt2 = Point(100, 50)
line = Line(pt, pt2)
line.draw(win)

pt = Point(100, 225)
pt2 = Point(100, 50)
line = Line(pt, pt2)
line.draw(win)

pt = Point(150, 215)
circ = Circle(pt, 40)
circ.draw(win)
circ.setFill("pink")
circ.setOutline(color_rgb(255, 30, 80))

pt = Point(50, 200)
circ = Circle(pt, 40)
circ.draw(win)
circ.setFill("pink")
circ.setOutline(color_rgb(255, 30, 80))

pt = Point(100, 225)
circ = Circle(pt, 40)
circ.draw(win)
circ.setFill("pink")
circ.setOutline(color_rgb(255, 30, 80))

win.getMouse()
win.close()
