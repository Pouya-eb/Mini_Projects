class ContactBook:
    """A class which represents a Contact Book.
    """
    def __init__(self) -> None:
        """Initialize contact book object.
        """
        self.contacts = dict()

    def add_contact(self, name: str, phone: str, email: str=None) -> str:
        """Adding a new contact to the contact book

        :param name: Name of the contact 
        :param phone: Phone number of the contact
        :param email: Email address of the contact, defaults to None
        :return: A message indicating whether the contact has been added or not
        """

        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email}
            return 'The contact is added successfully'
        else:
            return 'The contact already exists'
        
    def update_contact(self, name: str, phone: str=None, email: str=None) -> str:
        """Update a single contact

        :param name: Name of the contact to be updated
        :param phone: The new phone number for the contact , defaults to None
        :param email: The new email address for the contact, defaults to None
        :return: A message indicating wether the contact has been updated or not
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            return 'Contact is updated successfully'
        
        return 'Contact not found'
    
    def delete_contact(self, name: str) -> str:
        """Delete a single contact

        :param name: The name of the contact to be deleted
        :return: A message indicating wether the contact has been deleted or not
        """

        if name in self.contacts:
            del self.contacts[name]
            return 'Contact is deleted successfully'
        else:
            return 'Contact not found'
        
    def view_contacts(self):
        pass

contacts = ContactBook()

if __name__ == '__main__':
    pass