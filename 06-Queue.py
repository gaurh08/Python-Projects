# Queue is a linear structure which follows a particular order in which the operations are performed.
# The order is First In First Out (FIFO).
# The difference between stacks and queues is in removing. In a stack we remove the item the most recently added;
# in a queue, we remove the item the least recently added.

# Operations on Queue: Mainly the following four basic operations are performed on queue:
# 1. Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
# 2. Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed.
#   If the queue is empty, then it is said to be an Underflow condition.
# 3. Front: Get the front item from queue.
# 4. Rear: Get the last item from queue.

def createQueue():
    global queue
    queue = []
    print("Empty queue created.")
    return queue

def enqueue(queue):
    queue.append()


def main():
    T = int(input("Please enter number of test cases to run: "))
    while T:
        option = input("Enter 'n' to create new queue or e to exit program: " )
        if option = 'n':
            queue = createQueue()

if __name__ == '__main__':
    main()

