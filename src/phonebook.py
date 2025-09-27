class PhoneBook:
    def __init__(self):
        self.phonebook = {}

    def _check_contact_name(self,contact_name):
       return self.phonebook.__contains__(contact_name)

    def add_contact(self, contact_no, contact_name):
        if  self._check_contact_name(contact_name):
            raise ValueError("This contact is already registered")
        self.phonebook[contact_name] = contact_no

    def search_phonebook(self, contact_name):
        if not self.phonebook.__contains__(contact_name):
             raise ValueError("This contact is not registered")
        return contact_name, self.phonebook[contact_name]

    def delete_contact(self, contact_name):
        if not self.phonebook.__contains__(contact_name):
            raise ValueError("This contact is not registered")
        del self.phonebook[contact_name]
    def view_phonebook(self):
        return self.phonebook

    def edit_contact(self, contact_name):
        self.delete_contact(contact_name)
        self.add_contact(contact_name, contact_name)
    


