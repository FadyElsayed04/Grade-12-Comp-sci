#Name: Fady Elsayed
#Date: Dec 13th, 2021
#File Name: 5.1 1.py
#Description: A GUI that gets the aera or perimeter.

from graphics import * 
from button import *

#Create a window with width = 300 and height = 300 
win = GraphWin("Area and Perimeter", 300, 300)
win.setCoords(0, 0, 300, 300)
win.setBackground("green")

#Draws header
headerBox = Rectangle(Point(4, 240), Point(300, 296))
headerBox.draw(win)
headerBox.setFill("yellow")
headerBox.setOutline("blue")
headerBox.setWidth(4)
header = Text(Point(150, 270), "Enter length and width.\n Then click on \
'""'Area'""' or '""'Perimeter'""'.")
header.draw(win)
header.setStyle("bold")

#Draws output box
outputBox = Rectangle(Point(75, 60), Point(225, 90))
outputBox.draw(win)
outputBox.setFill("yellow")
outputBox.setOutline("blue")
outputBox.setWidth(4)

#Draws entry boxes
length = Entry(Point(100, 200), 10) 
length.draw(win)
width = Entry(Point(100, 150), 10) 
width.draw(win)

#Writes text
l = Text(Point(40, 200), "L:")
l.draw(win)
w = Text(Point(40, 150), "W:")
w.draw(win)

#Creates the buttons
areaButton = Button(win, Point(200, 200), 45, 30, "Area")
areaButton.activate()
perimeterButton = Button(win, Point(210, 150), 80, 30, "Perimeter")
perimeterButton.activate()
outputButton = Button(win, Point(150, 20), 50, 30, "Quit ")

#Gets mouse input
pt = win.getMouse()
while not areaButton.clicked(pt) and not perimeterButton.clicked(pt) \
      and not outputButton.clicked(pt):
    pt = win.getMouse() 
    
#converts entry to float
length = length.getText()
width = width.getText()
length = float(length)
width = float(width)

#prints output
if perimeterButton.clicked(pt):
    perimeter = length + width + length + width
    output = Text(Point(150, 75), ("Perimeter  is: " + str(perimeter )))
    output.draw(win)

else:
    area = length * width
    output = Text(Point(150, 75), ("Area is: " + str(area)))
    output.draw(win)

output.setStyle("bold")

#Closes window on mouse click and ends program
outputButton.activate()

#Gets mouse input
pt = win.getMouse()
while not outputButton.clicked(pt):
    pt = win.getMouse() 

if outputButton.clicked(pt):
    win.close()
