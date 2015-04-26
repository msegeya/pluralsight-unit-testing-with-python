import os

class Phonebook(object):
    """ Create Phonebook object"""

    def __init__(self):
        self.book = {}
        self.filename = 'phonebook.txt'
        self.file_cache = open(self.filename, 'w')

    def add(self, name, number):
        self.book[name] = number

    def lookup(self, name):
        return self.book[name]

    def names(self):
        return self.book.keys()

    def numbers(self):
        return self.book.values()

    def clear(self):
        self.book = {}
        self.file_cache.close()
        os.remove(self.filename)