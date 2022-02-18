# button.py
# Fady Elsayed
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def setFill(self, color):
        "Fills the button with a color"
        self.rect.setFill(color)
        
    def setOutline(self, color):
        "Sets outline to button"
        self.rect.setOutline(color)

    def move(self, dx, dy):
        "Moves button dx and dy pixels right and down"
        self.rect.move(dx, dy)
        self.label.move(dx, dy)
        self.xmax, self.xmin = self.xmax + dx, self.xmin + dx
        self.ymax, self.ymin = self.ymax + dy, self.ymin + dy

    def setFace(self, font):
        "Sets the face of the button."
        self.label.setFace(font)

    def setStyle(self, style):
        "Sets the style of the button's text"
        self.label.setStyle(style)

    def setFontColor(self, color):
        "Sets the font color"
        self.label.setFill(color)
