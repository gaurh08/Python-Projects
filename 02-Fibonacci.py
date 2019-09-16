# Fibonacci sequence generator program

def numValidation():
    """
    This function will validate if the number is positive otherwise customized error is shown to user.
    """
    while True:
        N = int(input("Please Enter any positive Integer: "))
        try:
            if N > 0:
                return N
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Please Enter a positive integer.')


def fib(num):
    """
    Recursively return next term to generate fibonacci sequence
    """
    if num==1:
        return [1,0]
    else:
        terms = fib(num-1)
        terms = terms[0]+terms[1],terms[0]
        return terms


def main():
    N = numValidation()
    fib(N)[1]


if __name__ == '__main':
    main()
