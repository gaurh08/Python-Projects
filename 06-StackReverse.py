# Reverse a stack using recursion
# Our task is to reverse a stack using recursion where we are not allowed to use loop function like while, for etc.
# we can only use loop to create a stack

def createStack():
    global stack
    stack = []
    print("Please enter 6 elements of stack:")
    for i in range(6):
        stack.append(int(input(f"{i}th element of stack:")))
    return stack

def popItem(stack, num):
    return stack.pop


def addItem(stack, num):
    stack.append(num)
    return stack


def reverseStack():



def main():
    print("Create stack to reverse.")
    stack = createStack()
    print("Our stack is ", stack)


if __name__ == '__main__':
    main()
