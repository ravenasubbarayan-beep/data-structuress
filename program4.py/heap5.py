def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(arr, value):
    arr.append(value)

    i = len(arr) - 1

    while i > 0:
        parent = (i - 1) // 2

        if arr[parent] < arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
        else:
            break

def delete(arr):
    if not arr:
        return None

    deleted = arr[0]
    arr[0] = arr[-1]
    arr.pop()

    if arr:
        heapify(arr, len(arr), 0)

    return deleted

heap = []

insert(heap, 20)
insert(heap, 50)
insert(heap, 30)
insert(heap, 40)
insert(heap, 10)

print("Heap after insertion:", heap)

print("Deleted:", delete(heap))

print("Heap after deletion:", heap)