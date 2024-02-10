'''
    By default all members of a class in python are Public and can be accessed from outside the class
'''

# Public class Example
class Person:
    favourite_show='Sherlock Holmes' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute


# accessing the Person attributes by creating object of a class

person=Person('Dhirendra', 30)
print(person.favourite_show)
print(person.name)
print(person.age)



