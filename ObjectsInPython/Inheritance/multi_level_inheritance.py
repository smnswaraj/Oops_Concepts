
# Multi-level Inheritance:

class Animal:  # Level 1
    def __init__(self, species):
        self.species = species
        print(f"Animal initialized. Species: {self.species}")

class Dog(Animal):  # Level 2
    def __init__(self, species, breed):
        super().__init__(species)  # Calls Animal's __init__
        self.breed = breed
        print(f"Dog initialized. Breed: {self.breed}")

class Puppy(Dog):  # Level 3
    def __init__(self, species, breed, age):
        super().__init__(species, breed)  # Calls Dog's __init__
        self.age = age
        print(f"Puppy initialized. Age: {self.age}")

# Create a Puppy object
puppy = Puppy("Canine", "Labrador", 3245)