# Implementation of stacks using Python:

def createStack():
    global stack
    stack = []
    return stack

def addItem(stack, num):
    stack.append(num)
    print(f'{num} is pushed into stack')

def removeItem(stack):
    num = stack.pop()
    print(f'{num} is popped from stack')

def isEmpty(stack):
    return len(stack) == 0

def checkTop(stack):
    print("Top element of stack is ", stack[-1])

def main():
    while True:
        option = input("Enter 'n' to create new empty stack or 'e' to exit program:")
        if option == 'n':
            createStack()
            while True:
                op = int(input("""
                Please choose from below operations on stack:
                1. Add Item, 2. Remove Item, 3. Peek, 4. Check if Empty, 5. Stop Operations
                """))
                if op == 1:
                    num = int(input("Enter Item to add into stack: "))
                    addItem(stack, num)
                elif op == 2:
                    removeItem(stack)
                elif op == 3:
                    checkTop(stack)
                elif op == 4:
                    isEmpty(stack)
                elif op == 5:
                    print("Current status of Stack is ", stack)
                    break
        else:
            print("Exit from Program")
            break


if __name__ == '__main__':
    main()
