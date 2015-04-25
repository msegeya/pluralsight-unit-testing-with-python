
class Phonebook(object):
    """Create Phonebook object"""
    
    def __init__(self):
        self.book = {}

    def add(self, name, number):
        self.book[name] = number

    def lookup_entry_by_name(self, name):
        return self.book[name]

        