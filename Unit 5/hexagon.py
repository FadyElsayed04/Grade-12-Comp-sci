# Name: Fady Elsayed
# Date: December 16th 2021
# File Name: hexagon.py
# Description: A class to show a GUI that displays a Hexagon, with a size,
# centre position, and colour of your choosing. Hexagon is the class created.
# There is also a main program to test the class.

from graphics import * 

# Process: Creates class called Hexagon.
class Hexagon:
    """ A class to show a GUI that displays a Hexagon, with a size,
    centre position, outline, width, and colour of the user's choosing. """
    
# Process: Creates function called __init__.
    def __init__(self, win, dx, dy, size):
        """ Sets varables and creates points for hexagoon"""
        
        self.size = size
        pt1 = Point(dx - size, dy)
        pt2 = Point(dx - size / 2, dy + size / 1.2)
        pt3 = Point(dx + size / 2, dy + size / 1.2)
        pt4 = Point(dx + size, dy)
        pt5 = Point(dx + size / 2, dy - size / 1.2)
        pt6 = Point(dx - size / 2, dy - size / 1.2)

# Process: Uses points above to draw Hexagon.
        self.poly = Polygon(pt1, pt2, pt3, pt4, pt5, pt6)
        self.poly.setFill("lightgray")
        self.poly.draw(win)
    
# Process: Creates function called move.       
    def move(self, dx, dy):
        """ Funtion to move the hexagon dx right and dy up"""
        
        self.poly.move(dx, dy)

# Process: Creates function called move.       

    def setFill(self, colour):
        """ Funtion to set the color inside of the hexagon"""
        self.poly.setFill(colour)
        
# Process: Creates function called setWidth.       
    def setWidth(self, pixels):
        """ Funtion to set the width of the outline for the hexagon"""
   
        self.poly.setWidth(pixels)

# Process: Creates function called setOutline.       
    def setOutline(self, colour):
        """ Funtion to set the outline of the hexagon"""
   
        self.poly.setOutline(colour)

# Process: Creates function called getSize.       
    def getSize(self):
        """ Funtion to return the size of the hexagon to the user"""

        return self.size

# Process: creates main function.
def main():
    """ Main function to test the Hexagon class"""
    
# Process: Creates a window with width = 300 and height = 300 
    win = GraphWin("Hexagon", 300, 300)
    win.setCoords(0, 0, 300, 300)

# Process: Tests class.
    gui = Hexagon(win, 150, 150, 50)

    gui.setFill("blue")
    gui.setOutline("red")
    gui.setWidth(5)
    gui.move(-30, 60)
    print(gui.getSize())

# Main Program:
main()


