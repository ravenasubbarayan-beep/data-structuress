bookings = [
    ["Arun", "Leo", 5, 750],
    ["Meena", "Jailer", 2, 300],
    ["Ravi", "Vikram", 4, 600],
    ["Divya", "Beast", 1, 150],
    ["Kumar", "Master", 3, 450]
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0][2]

    left = [x for x in arr[1:] if x[2] <= pivot]
    right = [x for x in arr[1:] if x[2] > pivot]

    return quick_sort(left) + [arr[0]] + quick_sort(right)

result = quick_sort(bookings)

print("SORTED BOOKING DETAILS")
print("Name\tMovie\tTickets\tAmount")

for b in result:
    print(b[0], "\t", b[1], "\t", b[2], "\t", b[3])