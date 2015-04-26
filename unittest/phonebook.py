
class Phonebook(object):
    """Create Phonebook object"""
    
    def __init__(self):
        self.book = {}

    def add(self, name, number):
        self.book[name] = number

    def lookup_entry_by_name(self, name):
        return self.book[name]

    def is_consistent(self):
        # Check if there are duplicates
        if len(self.book.values()) != len(set(self.book.values())):
            return False
        # Check no number is a prefix of any other number
        for p, n in enumerate(sorted(self.book.values())):
            for p2, n2 in enumerate(sorted(self.book.values())):
                if p != p2:
                    if n.startswith(n2):
                        return False
        return True

    def get_names(self):
        return self.book.keys()

    def get_numbers(self):
        return self.book.values()
        