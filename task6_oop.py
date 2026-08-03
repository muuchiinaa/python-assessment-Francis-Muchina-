task6_oop.py
 
Task 6: Object-Oriented Python
"""
 
 
class Animal:
    """Base class representing a generic animal."""
 
    species = "Unknown"   # (a) class variable
    counter = 0            # (d) tracks total instances created
 
    def __init__(self, name, sound):
        """(a) Initialize an animal with a name and sound."""
        self.name = name
        self.sound = sound
        self.__age = 0  # (f) private attribute (encapsulation)
        Animal.counter += 1  # increment shared instance counter
 
    def speak(self):
        """(b) Print the animal's name and the sound it makes."""
        print(f"{self.name} says {self.sound}")
 
    # (f) Getter and setter for the private __age attribute
    def get_age(self):
        """Return the animal's current age."""
        return self.__age
 
    def set_age(self, age):
        """Set the animal's age, rejecting invalid values."""
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")
 
 
class Dog(Animal):
    """(e) Subclass of Animal that overrides speak()."""
 
    def __init__(self, name):
        # Dogs always say "Woof", so sound is fixed here
        super().__init__(name, "Woof")
 
    def speak(self):
        """Override speak() with dog-specific behaviour."""
        print(f"{self.name} the dog barks: {self.sound}!")
 
 
def main():
    # (c) Create at least two Animal instances and call speak()
    cat = Animal("Whiskers", "Meow")
    cow = Animal("Bella", "Moo")
    cat.speak()
    cow.speak()
 
    # (e) Create a Dog instance (inherits from Animal, overrides speak)
    dog = Dog("Rex")
    dog.speak()
 
    # (d) Show the total number of Animal instances created
    print("Total animals created:", Animal.counter)
 
    # (f) Use the getter/setter to work with the private __age attribute
    dog.set_age(3)
    print(f"{dog.name}'s age is now {dog.get_age()}")
    dog.set_age(-5)  # invalid, will be rejected by the setter
 
 
if __name__ == "__main__":
    main()
