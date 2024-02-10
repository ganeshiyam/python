class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.items = []

    def enqueue(self, item):
        # Add the item to the back of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        # Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return self.items == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)
        

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())  # Should print 1
    print(queue.peek())  # Should print 2
    print(queue.is_empty())  # Should print False
    print(queue.size())  # Should print 2