from graphics import * 

win = GraphWin("calculator", 190, 180)
win.setCoords(0, 0, 190, 180)

win.setBackground(color_rgb(120, 132, 148))

pt = Point(45, 170)
pt2 = Point(145, 150)
output = Rectangle(pt, pt2)
output.draw(win)
output.setFill("white")
output.setOutline("white")

k = 1
for n in range(50, 120, 30):
    for i in range(10, 155, 35):
        pt = Point(i, n)
        pt2 = Point(i + 30, n + 20)
        box = Rectangle(pt, pt2)
        box.draw(win)
        box.setOutline("black")
        pt = Point(i + 15, n + 10)
        text = Text(pt, k)
        text.draw(win)
    
        if k == 3:
            k = "+"
        elif k == "+":
            k = "-"
        elif k == "-":
            k = 4
        elif k == 6:
            k = "*"
        elif k == "*":
            k = "/"
        elif k == "/":
            k = 7
        elif k == 9:
            k = "%"
        elif k == "%":
            k = "^"
        elif k != "^":
            k += 1

pt = Point(45, 40)
pt2 = Point(75, 20)
box = Rectangle(pt, pt2)
box.draw(win)
box.setOutline("black")
pt = Point(60, 30)
text = Text(pt, "0")
text.draw(win)

pt = Point(80, 40)
pt2 = Point(110, 20)
box = Rectangle(pt, pt2)
box.draw(win)
box.setOutline("black")
pt = Point(95, 30)
text = Text(pt, ".")
text.draw(win)

pt = Point(115, 40)
pt2 = Point(180, 20)
box = Rectangle(pt, pt2)
box.draw(win)
box.setOutline("black")
pt = Point(147, 30)
text = Text(pt, "=")
text.draw(win)

win.getMouse()
win.close()
