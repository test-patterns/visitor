from visitor import Visitor
from sauce import Sauce
from cheese import Cheese
from dough import Dough

class Surcharge(Visitor):
  def visit(self, visitable):
      visitable_type = type(visitable)
      if visitable_type == Sauce:
          print("Sauce item: Price with Surcharge")
          return visitable.getPrice() * 1.18
      elif visitable_type == Cheese:
          print("Cheese item: Price with Surcharge")
          return visitable.getPrice() * 1.30
      elif visitable_type == Dough:
          print("Dough item: Price with Surcharge")
          return visitable.getPrice() * 1.45
      else:
          raise TypeError
