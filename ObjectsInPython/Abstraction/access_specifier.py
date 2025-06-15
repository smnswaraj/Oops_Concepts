

# Most object-oriented programming languages have a concept of access control.
# Python doesn't do this.
# Technically, all methods and attributes on a class are publicly available. If
# we want to suggest that a method should not be used publicly, we can put a note in
# docstrings indicating that the method is meant for internal use only (preferably, with
# an explanation of how the public-facing API works!).

# By convention, we should also prefix an attribute or method with an underscore
# character, _. Python programmers will interpret this as "this is an internal variable,
# think three times before accessing it directly". But there is nothing inside the interpreter
# to stop them from accessing it if they think it is in their best interest to do so.

# There's another thing you can do to strongly suggest that outside objects don't access
# a property or method: prefix it with a double underscore, __. This will perform name
# mangling on the attribute in question. This basically means that the method can still be
# called by outside objects if they really want to do it, but it requires extra work and is a
# strong indicator that you demand that your attribute remains private. For example:

class SecretString:
    '''Class representing a secret string'''

    def __init__(self, plain_string, pass_phrase):
        self.plain_string = plain_string
        self.pass_phrase = pass_phrase
        self._name = "swaraj"
        self.__caste = "Mandal"

    def decrypt(self, passphrase):
        '''only show the plain_string if passphrase is correct.'''
        if passphrase == self.pass_phrase:
            return self.plain_string
        return None

    def getter(self):
        return self.__caste

class_obj = SecretString("my secret string", "password")
print(class_obj._name)     # "swaraj"
# print(class_obj.__caste) # error, not attribute __caste
print(class_obj.getter())  # Mandal

# It looks like it works; nobody can access our plain_text attribute without the
# passphrase, so it must be safe. Before we get too excited, though, let's see how
# easy it can be to hack our security:

# print(class_obj._SecretString__plain_string)

# When we use a double underscore, the property
# is prefixed with _<classname>. When methods in the class internally access the
# variable, they are automatically unmangled. When external classes wish to access
# it, they have to do the name mangling themselves. So, name mangling does not
# guarantee privacy, it only strongly recommends it.
















