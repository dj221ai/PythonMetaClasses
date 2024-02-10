"""
    1. The members of a class that are declared protected are only accessible to a class derived from it or within the class.
    2. This enables specific resources of the parent class to be inherited by the child class.
    3. No other environment is permitted access to it
    4. For using Protected modifier python uses single underscore '_' 
    5. one can even use property decorator for creating protected class

"""

# using single underscore

class Human:
    # protected class members
    _favourite_novel='The Adventures of Sherlock homes'   

    def __init__(self, name, age):
        # protected instance variable
        self._name=name
        self._age=age

    # protected method
    def _displayDetails(self):
        print("Name is: ", self._name)
        print("Age is: ", self._age)


# inheriting the Human class or subclass
class Person(Human):

    def __init__(self, name, age):
        super().__init__(name, age)


    # public method
    def show(self):
        
        # access protected class members directly
        # print("Favourite Novel is ", self._favourite_novel)

        # accessing protected instance members in protected methods
        self._displayDetails()



# accessing protected members
person=Person('Dhirendra', 30)
print("Favorite Novel is: ", person._favourite_novel)
person.show()




        



