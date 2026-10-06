bookings = [
    [105, "Ravi", "Leo", 3],
    [102, "Anu", "Jailer", 2],
    [104, "Kumar", "Vikram", 5],
    [101, "Priya", "Beast", 1],
    [103, "Arun", "Master", 4]
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0][0]

    left = [x for x in arr[1:] if x[0] < pivot]
    right = [x for x in arr[1:] if x[0] >= pivot]

    return quick_sort(left) + [arr[0]] + quick_sort(right)

result = quick_sort(bookings)

print("MOVIE BOOKING DETAILS")
print("ID\tName\tMovie\tTickets")

for b in result:
    print(b[0], "\t", b[1], "\t", b[2], "\t", b[3])