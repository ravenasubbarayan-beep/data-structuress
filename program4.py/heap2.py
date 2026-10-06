import heapq

heap = []

heapq.heappush(heap, 40)
heapq.heappush(heap, 20)
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 50)

print("Min Heap after insertion:", heap)

deleted = heapq.heappop(heap)

print("Deleted element:", deleted)
print("Heap after deletion:", heap)