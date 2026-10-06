queue = []

def enqueue():
    value = int(input("Enter element: "))
    queue.append(value)
    print(value, "inserted")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        value = queue.pop(0)
        print(value, "deleted")

def display():
    print("Queue:", queue)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")