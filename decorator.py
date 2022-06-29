# basic way

def halfAdd(func):
    def divFunc(a,b):
        a=a//2
        b=b//2
        return func(a,b)
    return divFunc

@halfAdd
def add(a,b):
    print(a+b)


add(4,4)  

