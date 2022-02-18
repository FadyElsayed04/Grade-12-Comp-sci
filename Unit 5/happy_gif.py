from graphics import * 

#Create a window with width = 300 and height = 300
win = GraphWin("Program Name", 500, 500)
win.setCoords(0, 0, 500, 500)

#Display an image. Constructs an image centered at the point
#using the file happy.gif
image = Image(Point(250, 250), "happy.gif")
image.draw(win)

#Closes window on mouse click and ends program
win.getMouse()
win.close()
