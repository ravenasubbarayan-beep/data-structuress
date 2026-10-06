

bookings = [
    ["Ravi", "Leo", 4, 600],
    ["Anu", "Jailer", 2, 300],
    ["Kumar", "Vikram", 5, 750],
    ["Priya", "Beast", 3, 450],
    ["Arun", "Master", 1, 150]
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0][3]
    left = [x for x in arr[1:] if x[3] <= pivot]
    right = [x for x in arr[1:] if x[3] > pivot]

    return quick_sort(left) + [arr[0]] + quick_sort(right)

bookings = quick_sort(bookings)

print("MOVIE TICKET BOOKINGS")
print("Name\tMovie\tTickets\tPrice")

for b in bookings:
    print(b[0], "\t", b[1], "\t", b[2], "\t", b[3])

  