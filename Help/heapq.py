import queue as Q

q = Q.PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
while not q.empty():
	print(q.get())

q.put((10, "ten"))
q.put((1, "one"))
q.put((5, "five"))
while not q.empty():
	print(q.get())

import heapq

heap = []
heapq.heappush(heap, (1, "one"))
heapq.heappush(heap, (10, "ten"))
heapq.heappush(heap, (5, "five"))

print("//")

for x in heap:
	print(x)

heapq.heappop(heap)

for x in heap:
	print(x)

print(heap[0])



#Transform list to heap O(N)

heap = [(1, "one"), (10, "ten"), (5, "five")]
heapq.heapify(heap)
for x in heap:
	print(x)

heap[1] = (9, "nine")
for x in heap:
	print(x)

