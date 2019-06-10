#
def squreOfNumbers(nums):
    for i in range (len(nums)):
        nums[i]=nums[i]*nums[i]
    print("nums:",nums)

numbers=[10,20,30,40]
squreOfNumbers(numbers)
print("numbers is :",numbers)