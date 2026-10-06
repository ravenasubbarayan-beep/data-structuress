MAX = 5
stack = [None] * MAX
top = -1

def push(value):
    global top
    if top == MAX - 1:
        print("Stack Overflow")
    else:
        top += 1
        stack[top] = value
        print(value, "pushed")

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        print("Popped:", stack[top])
        top -= 1

def peek():
    if top == -1:
        print("Stack is empty")
    else:
        print("Top element:", stack[top])

push(10)
push(20)
push(30)

print("Stack:", stack[:top + 1])
peek()
pop()
print("Stack:", stack[:top + 1])