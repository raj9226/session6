#Default agrgument values in functions
def addNumbers(num1,num2,num3=0):
    sum=num1+num2+num3
    print("su is:",sum)
print("add number is:",addNumbers)
#Update operation on function
def addNumbers(num1,num2,num3,num4):
    num3=num1+num2+num3+num4
    print("su is:",num3)
print("addNumbers is:",addNumbers)
#addNumbers(10,20)
#addNumbers(10,20,30)