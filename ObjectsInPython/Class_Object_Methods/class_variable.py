

# CLASS VARIABLE

class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

# This example introduces us to class variables. The all_contacts list, because it is
# part of the class definition, is shared by all instances of this class. This means that
# there is only one Contact.all_contacts list, which we can access as Contact.all_contacts.
# Less obviously, we can also access it as self.all_contacts on any object
# instantiated from Contact.

# Be careful with this syntax, for if you ever set the variable using
# self.all_contacts, you will actually be creating a new instance
# variable associated only with that object. The class variable will still
# be unchanged and accessible as Contact.all_contacts.