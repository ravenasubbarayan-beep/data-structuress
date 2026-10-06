# Stack using Class

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is Empty"

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "Stack is Empty"


s = Stack()

s.push(5)
s.push(15)
s.push(25)

print("Stack:", s.stack)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Stack after Pop:", s.stack)