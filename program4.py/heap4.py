import heapq

heap = []

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        heapq.heappush(heap, value)
        print("Inserted:", value)

    elif choice == 2:
        if heap:
            print("Deleted:", heapq.heappop(heap))
        else:
            print("Heap is empty")

    elif choice == 3:
        print("Heap:", heap)

    elif choice == 4:
        print("Program ended")
        break

    else:
        print("Invalid choice")