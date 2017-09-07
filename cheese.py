from visitable import Visitable

class Cheese(Visitable):
    def __init__(self, item):
        self._price = item

    def getPrice(self):
        return self._price

    def accept(self, visitor):
        return visitor.visit(self)
