class Dough(Visitable):
    def Dough(item):
        self._price = item

    def getPrice:
        return self._price

    def accept(self, Visitor):
        return Visitor.visit(self)
