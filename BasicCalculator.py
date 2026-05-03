# Calculate the of array
def arraySum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def add2Array(arr, arr2):
    sumArray = arr + arr2
    return sumArray

# Calculate sum
def sum(num1, num2):
    return num1 + num2

# Calculate the difference
def substraction(num1, num2):
    return num1 - num2

# Calculate product
def multiply(num1, num2):
    return num1 * num2

# Calculate division
def divide(num1, num2):
    if num2 > 0:
        return num1 / num2
    else:
      return "Error"

n = 0

# Stop infinite loop when user enter 999
while n != 999:
    # Show UI
    print("\t\t----------Basic Calculator-----------\n")
    print("What operation would you like to do? (Enter 999 to stop the program)\n\n1. Addition\n2. Substraction\n3. Multiply\n4. Divide")
    n = int(input())

    # Get user info
    if n >= 1 and n <= 4:
        n1 = int(input("Enter the number: "))
        n2 = int(input("Enter the second number: "))

    # Determine which operation to conduct
    if n == 1:
        print("The sum is", sum(n1, n2))
    elif n == 2:
        print(substraction(n1, n2))
    elif n == 3:
        print(multiply(n1, n2))
    elif n == 4:
        print(divide(n1, n2))
    else:
        if n == 999:
            print("Program Canceled!")
        else:
            print("Error")

"""""
nums = [1, 2, 3, 4]
nums2 = [3, 7, 5]

print(arraySum(nums))
print(add2Array(nums, nums2))
"""