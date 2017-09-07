""" Sample problem featuring the visitor pattern. """

class Visitor(object):
    """ An interface for a visitor object """

    def visit(self, visitable):
        """ Base method to visit an object """
        raise NotImplementedError
