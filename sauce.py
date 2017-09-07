class Sauce(Visitable):
    def Sauce(item):
        self._price = item

    def getPrice(self):
        return self._price

    def accept(self, Visitor):
        return Visitor.visit(self)
