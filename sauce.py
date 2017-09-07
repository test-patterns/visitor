from visitable import Visitable

class Sauce(Visitable):
    def __init__(self, price):
        self._price = price

    def getPrice(self):
        return self._price

    def accept(self, visitor):
        return visitor.visit(self)
