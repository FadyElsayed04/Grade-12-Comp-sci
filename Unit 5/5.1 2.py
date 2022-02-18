#Name: Fady Elsayed
#Date: Dec 13th, 2021
#File Name: 5.1 2.py
#Description: GUI that converts the temperature inputted to fahrenheit.

from graphics import * 
from button import *

#Create a window with width = 300 and height = 300 
win = GraphWin("Area and Celsius Converter", 300, 300)
win.setCoords(0, 0, 300, 300)

#Writes text
celsius = Text(Point(100, 250), "Celsius Temperature:")
celsius.draw(win)
fahrenheit = Text(Point(100, 50), "Fahrenheit Temperature:")
fahrenheit.draw(win)

#creates entry
celsius = Entry(Point(205, 250), 5) 
celsius.draw(win)

#Creates button
convert = Button(win, Point(150, 150), 100, 100, "Convert IT")
convert.activate()

#converts entry to float
pt = win.getMouse()
while not convert.clicked(pt):
    pt = win.getMouse() 

celsius = celsius.getText()
celsius = float(celsius)

#prints output
output = Text(Point(205, 50), (round(celsius * 1.8 + 32, 2)))
output.draw(win)

#Closes window on mouse click and ends program
win.getMouse()
win.close()
