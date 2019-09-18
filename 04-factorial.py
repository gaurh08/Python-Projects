# Program to calculate factorial of any given number.
# 1. The program should run for N number of test cases
# 2. The program should handle cases of zero and negative/positive numbers


def fact(num):
    if num < 0:
        return "Sorry, factorial of a negative number doesn't exist"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)


# Driver Code:
N = int(input("Please enter number of test cases: "))
while N:
    number = int(input("Please enter number to find factorial: "))
    print("Factorial of given number is: ", fact(number))
    N -= 1
