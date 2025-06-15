

# How to import something from another module/file ?
# method 1
import constructor_vs_initializer

db_obj = constructor_vs_initializer.DataBase()

# method 2
from constructor_vs_initializer import DataBase
db_obj_1 = DataBase()


# A package is a collection of
# modules in a folder. The name of the package is the name of the folder. All we need to
# do to tell Python that a folder is a package is place a (normally empty) file in the folder
# named __init__.py. If we forget this file, we won't be able to import modules from
# that folder.

# In Python 3, there are two ways of importing modules: absolute imports
# and relative imports.
# 1. Absolute import 2. Relative import

#  Absolute import: from package_A.package_B.module_Y import class_A
# Relative import : from ../../package_C.moduleD import class_X

# Indeed, assuming the packages are available to Python, it will be
# able to import them. For example, the packages can also be installed to the Python
# site packages folder, or the PYTHONPATH environment variable could be customized
# to dynamically tell Python what folders to search for packages and modules it is
# going to import.

# If __init__.py file that defines a directory as a package? This file can
# contain any variable or class declarations we like, and they will be available as part of
# the package. In our example, if the ecommerce/__init__.py file contained this line:
# from .database import db
# We can then access the db attribute from main.py or any other file using this import:
# from ecommerce import db

# It might help to think of the __init__.py file as if it was an ecommerce.py file if that
# file were a module instead of a package. This can also be useful if you put all your
# code in a single module and later decide to break it up into a package of modules.
# The __init__.py file for the new package can still be the main point of contact for
# other modules talking to it, but the code can be internally organized into several
# different modules or subpackages.


# Classes can be defined anywhere. They are typically defined at
# the module level, but they can also be defined inside a function or method, like this:











