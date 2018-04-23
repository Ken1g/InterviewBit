from heapq import heappush, heappop

pq = [(0, "A")]
cur = heappop(pq)
print(cur)
heappush(pq, (10, "V"))
cur = heappop(pq)
print(cur)

heappush(pq, (2, "C"))
heappush(pq, (1, "f"))
heappush(pq, (3, "ewe"))
cur = heappop(pq)
print(cur)
