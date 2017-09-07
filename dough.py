from visitable import Visitable

class Dough(Visitable):
    def __init__(self, item):
        self._price = item

    def getPrice(self):
        return self._price

    def accept(self, visitor):
        return visitor.visit(self)
