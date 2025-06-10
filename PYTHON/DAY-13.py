class Stack:
    def __init__(self):
        self.stack = []  # Empty list = empty stack

    def push(self, item):
        # Add item to the top of stack
        self.stack.append(item)

    def pop(self):
        # Remove top item if not empty
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        # Peek at the top item without removing
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Stack testing zone 🎯
s = Stack()
s.push(10)
s.push(20)
print("Top item:", s.peek())  
s.pop()
print("Top item after pop:", s.peek())  