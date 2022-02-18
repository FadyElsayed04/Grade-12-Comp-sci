import random

class MSDie:

    """A MSDie is a multisided die with n sides.
    It can be rolled or a value can be set for the die."""

    def __init__ (self, n):
        """ Creates a multisided die with n sides, eg:
        mdie = MSDie(18) """ 
        self.sides = n
        self.setValue(1)

    def roll(self):
        """Rolls the n-sided die"""
        self.value = random.randint(1, self.sides)

    def setValue(self, value):
        """Sets value of die to value"""
        self.value = value

    def getValue(self):
        """Returns the value of the die"""
        return self.value

    

        
