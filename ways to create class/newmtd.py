class NewMtdWay:
    def __new__(self, *args, **kwargs):
        print("creating an object !!")
        return super(NewMtdWay, self).__new__(self, *args, **kwargs)
    
    def __init__(self, *args, **kwargs) -> None:
        print("instantiating")
        super(NewMtdWay, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return "New Method Call"


newm=NewMtdWay()
print(newm)