# This program will be used to calculate value of pi up to Nth Digit.
# Nth digit will be input from user

import math
import sys
from decimal import *

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)


# Below function will calculate factorial of a number using recursion:
def factorial(num):
    if not num:
        return 1
    else:
        return num * factorial(num - 1)


def getIteratedValue(k):
    k = k + 1
    getcontext().prec = k
    sum = 0
    for k in range(k):
        first = factorial(6 * k) * (13591409 + 545140134 * k)
        down = factorial(3 * k) * (factorial(k)) ** 3 * (640320 ** (3 * k))
        sum += first / down
    return Decimal(sum)


def getValueOfPi(k):
    iter = getIteratedValue(k)
    up = 426880 * math.sqrt(10005)
    pi = Decimal(up) / iter

    return pi


def shell():
    print("""Welcome to Pi Calculator. Please Enter the number of digits upto which the value of Pi should "
           "be calculated or enter quit to exit""")

    while True:
        print(">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("You did not enter a number. Try again")
        else:
            print(getValueOfPi(int(entry)))


if __name__ == '__main__':
    shell()
