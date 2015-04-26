
class Phonebook(object):
    """ Create Phonebook object"""

    def __init__(self):
        self.book = {}

    def add(self, name, number):
        self.book[name] = number

    def lookup(self, name):
        return self.book[name]