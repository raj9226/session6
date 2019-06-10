#Passing Values
def squareOfNumber(num):
    sqr=num*num
    print("square of {} is {}".format(num,sqr))

n=11
squareOfNumber(n)
print("n is:",n)

#modifying num will not change n

def addNumber(a,b,c):
    d=a+b++c
print(addNumber(a=10,c=20,b=30))

