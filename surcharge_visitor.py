class Surcharge(Visitor):
  def Surcharge():
    pass
    
  def visit(Sauce sauceItem):
    print("Sauce item: Price with Surcharge")
    return(sauceItem.getPrice() * 1.18)

  def visit(Cheese cheeseItem):
    print("Cheese item: Price with Surcharge")
    return(cheeseItem.getPrice() * 1.30)

  def visit(Dough doughItem):
    print("Dough item: Price with Surcharge")
    return(doughItem.getPrice() * 1.45)
