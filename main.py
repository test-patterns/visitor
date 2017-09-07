from surcharge_visitor import Surcharge
from sauce import Sauce
from cheese import Cheese
from dough import Dough

def main():
    priceCalc = Surcharge()
    sauce = Sauce(2.00)
    cheese = Cheese(3.00)
    dough = Dough(4.00)

    print(sauce.accept(priceCalc))
    print(cheese.accept(priceCalc))
    print(dough.accept(priceCalc))

if __name__ == "__main__":
    main()
