class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Popped:", self.top.data)
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.peek()
s.pop()
s.peek()