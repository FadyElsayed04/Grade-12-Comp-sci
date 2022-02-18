# Fady Elsayed

from graphics import * 


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self, rank):
        return self.rank

    def getSuit(self, rank):
        return self.suit

    def __str__(self):      
# Process: Ranks.
        if self.rank == 1:
            self.rank = "Ace"
        elif self.rank == 2:
            self.rank = "Two"
        elif self.rank == 3:
            self.rank = "Three"
        elif self.rank == 4:
            self.rank = "Four"
        elif self.rank == 5:
            self.rank = "Five"
        elif self.rank == 6:
            self.rank = "Six"
        elif self.rank == 7:
            self.rank = "Seven"
        elif self.rank == 8:
            self.rank = "Eight"
        elif self.rank == 9:
            self.rank = "Nine"
        elif self.rank == 10:
            self.rank = "Ten"
        elif self.rank == 11:
            self.rank = "Jack"
        elif self.rank == 12:
            self.rank = "Queen"
        elif self.rank == 13:
            self.rank = "King"
            
# Process: Suits.
        if self.suit == "d":
            self.suit = "Diamonds"
        elif self.suit == "c":
            self.suit = "Clubs"
        elif self.suit == "h":
            self.suit = "Hearts"
        elif self.suit == "s":
            self.suit = "Spades"
            
        string = (self.rank + " of " + self.suit)
        
# Output: returns string.        
        return string 
