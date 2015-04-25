
import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def tearDown(self):
        pass

    def test_create_phonebook(self):
        phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        phonebook = Phonebook()
        phonebook.add('Bob', '12345')
        self.assertEqual('12345', phonebook.lookup_entry_by_name('Bob'))

    def test_missing_entry_raises_KeyError(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup_entry_by_name('missing')

    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        phonebook = Phonebook()
        self.assertTrue(phonebook.is_consistent())


if __name__ == '__main__':
    unittest.main()