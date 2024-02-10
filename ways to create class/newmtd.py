class NewMtdWay:
    def __new__(cls, *args, **kwargs):
        print("creating an object !!")
        return super(NewMtdWay, cls).__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs) -> None:
        print("instantiating")
        super(NewMtdWay, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return "New Method Call"


newm=NewMtdWay()
print(newm)