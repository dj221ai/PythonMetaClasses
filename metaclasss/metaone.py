from typing import Any


class MetaOne(type):

    def __call__(cls, *args, **kwds):
        instance = super(MetaOne, cls).__call__(*args, **kwds)
        return instance
    
    def __init__(cls, name, bases, attr):
        super(MetaOne, cls).__init__(name, bases, attr)


class Custom(metaclass=MetaOne):
    def __init__(self):
        pass

m=Custom()
print(m)



