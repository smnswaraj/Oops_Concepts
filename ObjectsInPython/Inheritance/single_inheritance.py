

# Inheritance

# Technically, every class we create uses inheritance. All Python classes are subclasses
# of the special class named object. This class provides very little in terms of data and
# behaviors (the behaviors it does provide are all double-underscore methods intended
# for internal use only), but it does allow Python to treat all objects in the same way.

# If we don't explicitly inherit from a different class, our classes will automatically
# inherit from object.

class MyClass(object):
    pass

# Inherit a built-in object. Example: list


class ContactList(list):

    def search(self, name):
        found_contacts = []
        for contact in self:
            # here self is a list object, i.e; ContactList is as list object.
            if contact.name == name:
                found_contacts.append(contact)
        return found_contacts

class Contacts:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)
        # self.all_contacts.append(self)  -> It is also valid

# So here, instead of using simple list, used ContactList()
# because it has the list properties inherited.

# Creating an empty list with [] is actually a shorthand for creating an
# empty list using list().

# In reality, the [] syntax is actually so-called syntax sugar that calls the list()
# constructor under the hood. The list data type is a class that we can extend.
# In fact, the list itself extends the object class:
# isinstance([], object) -> True

# Most built-in types can be similarly extended. Commonly extended built-ins are
# object, list, set, dict, file, and str. Numerical types such as int and float
# are also occasionally inherited from.

# Any method can be overridden, not just __init__.

# What we really need is a way to execute the original __init__ method on the
# Contact class. This is what the super function does; it returns the object as an
# instance of the parent class, allowing us to call the parent method directly

# class Friend(Contacts):
#
#     def __init__(self, name, email, phone):  -> error: super class init missing.
#         self.name = name
#         self.email = email
#         self.phone = phone

class Friend(Contacts):

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

# This example first gets the instance of the parent object using super, and calls
# __init__ on that object, passing in the expected arguments. It then does its own
# initialization, namely, setting the phone attribute.

# A super() call can be made inside any method, not just __init__. This means all
# methods can be modified via overriding and calls to super.














