heap = []

def insert(value):
    heap.append(value)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2

        if heap[parent] < heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break

def delete():
    if len(heap) == 0:
        print("Heap is empty")
        return

    deleted = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    i = 0

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(heap) and heap[left] > heap[largest]:
            largest = left

        if right < len(heap) and heap[right] > heap[largest]:
            largest = right

        if largest == i:
            break

        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest

    print("Deleted:", deleted)

insert(25)
insert(45)
insert(15)
insert(35)
insert(55)

print("Heap:", heap)

delete()

print("After deletion:", heap)