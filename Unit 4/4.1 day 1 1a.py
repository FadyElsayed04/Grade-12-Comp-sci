from graphics import * 

win = GraphWin("Face", 200, 150)
win.setCoords(0, 0, 200, 150)

pt = Point(100, 125)
tx = Text(pt, "Click anywhere to quit")
tx.draw(win)

pt1 = Point(120, 50)
tx1 = Text(pt1, "A face")
tx1.draw(win)

pt2 = Point(50, 50)
circ = Circle(pt2, 30)
circ.draw(win)
circ.setFill("yellow")

pt3 = Point(37, 32)
pt4 = Point(63, 45)
ovel = Oval(pt3, pt4)
ovel.draw(win)
ovel.setFill("red")

pt5 = Point(38, 55)
circ = Circle(pt5, 6)
circ.draw(win)
circ.setFill("blue")

pt6 = Point(55, 55)
pt7 = Point(67, 55)
line = Line(pt6, pt7)
line.draw(win)
line.setOutline("black")
line.setWidth(3)

win.getMouse()
win.close()
