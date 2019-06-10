#variable arguments
def addNumber(*args):

    print(args)
    print(type(args))
    sum=0
    for n in args:
        sum=sum+n
    print("the sum is:",sum)
addNumber(10,20,30)
"""
def addNumber(tpl):

    print(tpl)
    print(type(tpl))
addNumber((10,20,30))
"""