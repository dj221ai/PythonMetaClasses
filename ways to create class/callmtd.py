from typing import Any


class CallMtdWay:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super(CallMtdWay, self).__call__(self, *args, **kwds)
    
    def __str__(self) -> str:
        return "Using Call Method"
    

call=CallMtdWay()
print(call)