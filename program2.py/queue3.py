size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(value):
    global front, rear

    if (rear + 1) % size == front:
        print("Circular Queue is Full")
        return

    if front == -1:
        front = 0

    rear = (rear + 1) % size
    queue[rear] = value
    print(value, "inserted")

def dequeue():
    global front, rear

    if front == -1:
        print("Circular Queue is Empty")
        return

    value = queue[front]
    queue[front] = None

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size

    print(value, "deleted")

def display():
    print("Circular Queue:", queue)


enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)

display()

dequeue()
dequeue()

enqueue(50)
enqueue(60)

display()