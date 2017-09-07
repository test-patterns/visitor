#!/usr/bin/env python
""" Sample problem featuring the visitor pattern. """

from cheese import Cheese
from dough import Dough
from sauce import Sauce
from surcharge import Surcharge

def main():
    """ Execute the program """
    surcharge = Surcharge()
    sauce = Sauce(2.00)
    cheese = Cheese(3.00)
    dough = Dough(4.00)

    print(sauce.accept(surcharge))
    print(cheese.accept(surcharge))
    print(dough.accept(surcharge))

if __name__ == "__main__":
    main()
