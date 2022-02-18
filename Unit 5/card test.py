#Name: Fady Elsayed
#Date: Dec 15th 2021
#File Name: card test.py
#Description: This file contains the program that tests the cards class.

from Card import *
import random
from graphics import *


win = GraphWin("Display Hand", 400, 400)
win.setCoords(0,0,300,300)

win.setBackground("dark green")
x = 0

for i in range (1,6):
    random_rank = random.randint(1,13)
    random_suit = random.choice(["h","c", "d", "s"])
    card = Card(random_rank, random_suit)
    
    print (card.__str__())
    
    card_type = random_suit + str(random_rank) + ".png"
    
    pt = Point(270 - x, 150)
    card.draw(win, pt, card_type)
    
    x += 60

win.getMouse()
win.close()
