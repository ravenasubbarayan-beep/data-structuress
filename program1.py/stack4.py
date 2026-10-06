stack = []

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.append(value)
        print(value, "pushed")

    elif choice == 2:
        if not stack:
            print("Stack Underflow")
        else:
            print("Popped:", stack.pop())

    elif choice == 3:
        if not stack:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        print("Stack:", stack)

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")