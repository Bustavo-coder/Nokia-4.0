import unittest
from src import phonebook
class TestFunction(unittest.TestCase):
    def setUp(self):
        self.phonebook = phonebook.PhoneBook()
    def test_that_when_i_add_a_new_contact_it_got_added(self):
        self.phonebook.add_contact("08121844363", "Ade")


    def test_that_when_i_tried_storing_a_contact_that_exist_before_to_my_contact(self):
            self.phonebook.add_contact("08121844363", "Ade")
            self.assertRaises(ValueError, self.phonebook.add_contact, "O8121844363", "Ade")


    def test_that_when_i_search_for_a_contact_it_display_my_contact(self):
            self.phonebook.add_contact("08121844363", "Ade")
            result = self.phonebook.search_phonebook("Ade")
            self.assertEqual(result,("Ade","08121844363"))


    def test_that_when_i_search_for_a_contact_that_is_invalid(self):
        self.phonebook.add_contact("08121844363", "Ade")
        self.assertRaises(ValueError, self.phonebook.search_phonebook, "Qudus")

    def test_that_when_i_delete_a_contact_it_does_not_exist_again(self):
        self.phonebook.add_contact("08121844363", "Ade")
        self.phonebook.add_contact("07045052162", "Qudus")
        self.phonebook.add_contact("09027100266", "Yemi")
        self.phonebook.delete_contact("Qudus")
        result = self.phonebook.view_phonebook()
        dict_n = {"Ade" :"08121844363","Yemi" : "09027100266"}
        self.assertEqual(result, dict_n)

    def test_that_when_i_delete_a_contact_that_is_invalid(self):
        self.phonebook.add_contact("08121844363", "Ade")
        self.assertRaises(ValueError,self.phonebook.delete_contact,"quwam")



