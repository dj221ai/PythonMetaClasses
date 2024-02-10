"""
    1. The members of a class that are declared private are accessible within the class only.
    2. private access modifier is the most secure access modifier
    3. Double underscore '__' is used for declaring the private modifiers

    Note:- Although the private members can not be accessed directly but can be accessed indirectly in python using the concept of name mangling    
"""


class Employee:

    # private members of class
    __language=None
    __name=None
    __age=None


    def __init__(self, name, age, language) -> None:
        self.__name=name
        self.__age=age
        self.__language=language

    # private methods
    def __displayDetails(self):
        print("Name is: ", self.__name)
        print("Age is: ", self.__age)
        print("Language working on is: ", self.__language)

    # public method to fetch values
    def access(self):
        self.__displayDetails()



emp=Employee("Dhirendra", 30, "Python")
# print(emp.__dir__())

# accessing the private vairable using mangling in python
# print(emp._Employee__language)

emp.access()



