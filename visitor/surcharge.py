""" Sample problem featuring the visitor pattern. """

from cheese import Cheese
from dough import Dough
from sauce import Sauce
from visitor import Visitor

class Surcharge(Visitor):
    """ An ingredient surcharge """

    def visit(self, visitable):
        """ Visits an object """
        visitable_type = type(visitable)
        if visitable_type == Sauce:
            print("Sauce item: Price with Surcharge")
            return visitable.get_price() * 1.18
        elif visitable_type == Cheese:
            print("Cheese item: Price with Surcharge")
            return visitable.get_price() * 1.30
        elif visitable_type == Dough:
            print("Dough item: Price with Surcharge")
            return visitable.get_price() * 1.45
        else:
            raise TypeError
