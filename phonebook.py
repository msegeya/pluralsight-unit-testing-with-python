
class Phonebook(object):
    """Create Phonebook object"""
    
    def __init__(self):
        self.book = {}

    def add(self, name, number):
        self.book[name] = number

    def lookup_entry_by_name(self, name):
        return self.book[name]

    def is_consistent(self):
        return True

    def get_names(self):
        return self.book.keys()

    def get_numbers(self):
        return self.book.values()
        