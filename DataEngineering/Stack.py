class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.items = []
        pass

    def push(self, item):
        # Push the item onto the stack
        self.items.append(item)
        pass

    def pop(self):
        # Remove and return the item at the top of the stack
        if not self.is_empty():
            return self.items.pop()
        pass

    def peek(self):
        # Return the item at the top of the Stack without removing it
        if not self.is_empty():
            return self.items[-1]
        pass

    def is_empty(self):
        # Return True if the stack id empty, False otherwise
        return len(self.items) == 0
        pass

    def size(self):
        # Return the number of items in the stock
        return len(self.items)
        pass


if __name__ == "__main__":
    stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)

    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())
