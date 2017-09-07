""" Sample problem featuring the visitor pattern. """

class Visitable(object):
    """ An interface for visitable objects """

    def accept(self, visitor):
        """ Base method to accept a visitor """
        raise NotImplementedError
