
bookings = [
    ["Kumar", "Leo", 2, 300],
    ["Anu", "Jailer", 4, 600],
    ["Ravi", "Vikram", 1, 150],
    ["Divya", "Beast", 3, 450],
    ["Meena", "Master", 5, 750]
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0][0]

    left = [x for x in arr[1:] if x[0] < pivot]
    right = [x for x in arr[1:] if x[0] >= pivot]

    return quick_sort(left) + [arr[0]] + quick_sort(right)

result = quick_sort(bookings)

print("BOOKINGS SORTED BY CUSTOMER")
print("Name\tMovie\tTickets\tAmount")

for b in result:
    print(b[0], "\t", b[1], "\t", b[2], "\t", b[3])