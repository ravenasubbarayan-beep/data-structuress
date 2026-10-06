bookings = [
    ["Ravi", "Vikram", 2, 300],
    ["Anu", "Leo", 3, 450],
    ["Kumar", "Master", 1, 150],
    ["Priya", "Jailer", 5, 750],
    ["Arun", "Beast", 4, 600]
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0][1]

    left = [x for x in arr[1:] if x[1] < pivot]
    right = [x for x in arr[1:] if x[1] >= pivot]

    return quick_sort(left) + [arr[0]] + quick_sort(right)

result = quick_sort(bookings)

print("BOOKINGS SORTED BY MOVIE")
print("Name\tMovie\tTickets\tAmount")

for b in result:
    print(b[0], "\t", b[1], "\t", b[2], "\t", b[3])