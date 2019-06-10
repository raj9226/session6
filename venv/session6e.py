#Keyword Arguments
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun(a=10,b=20,name="John") #key must not be a number