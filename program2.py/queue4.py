class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(value, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        value = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(value, "deleted")

    def display(self):
        print("Queue:", self.queue)


cq = CircularQueue(4)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

cq.display()

cq.dequeue()

cq.enqueue(40)
cq.display()