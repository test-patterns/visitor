""" Sample problem featuring the visitor pattern. """

from visitable import Visitable

class Cheese(Visitable):
    """ The Cheese ingredient """
    def __init__(self, price):
        self._price = price

    def get_price(self):
        """ Gets the price of the ingredient """
        return self._price

    def accept(self, visitor):
        """ Accepts a visitor """
        return visitor.visit(self)
