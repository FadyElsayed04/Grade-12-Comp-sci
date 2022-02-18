from graphics import *
import random

class FancyDie:

    """A FancyDie is a die widget that displays one of the six
    standard sides of a die using a user defined list of images.
    The die can be rolled or a value can be set for the die."""

    def __init__(self, win, center, images, color, width):
        """ Creates a die widget, eg:
        die = FancyDie(myWin, centerPoint, image_files) """
        
        self.center = center
        self.win = win
        self.images = images
        self.setValue(1)

    

    def roll(self):
        """Rolls the n-sided die"""
        self.value = random.randint(1, 6)
        self.image = Image(self.center, self.images[self.value-1])
        self.image.draw(self.win)

    def setValue(self, value):
        """Sets value of die to value"""
        self.value = value
        self.image = Image(self.center, self.images[self.value-1])
        self.image.draw(self.win)

    def getValue(self):
        """Returns the value of the die"""
        return self.value

    def setBackground(self, color):
        """Sets the background color"""
        self.setBackground(color)

    def setOutline(self, color):
        """Sets the Outline"""
        self.setOutline(color)

    def setWidth(self, width):
        """ sets the width"""
        self.setWidth(width)
