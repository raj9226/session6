#functions--f(x)=x*x
#           f(2)=2*2=4
#methods/procedures/rotines
"""
Function
1.name
2.input(may or may not)/paramter/argument
3.return(myormay not)/acknowledgment
4.definition->sequence

Loop
    where we write statement
    which are repeated again again
why function
           Group of statement/logic which has to
           be executed again and again
Modularizations something which we are doing
in our program to simplify the process
"""


def addNumbers(num1,num2):
    num3=num1+num2
    #print("sum of {} and {} is{}".format(num1,num2,num3))
    return num3

result=addNumbers(10,20) #Exexution of addNumber function
print("sum is:",result)
print(addNumbers(10,30))
print("sum is:",addNumbers(10,40))
#addNumbers(10,30)
#addNumbers(30,20)