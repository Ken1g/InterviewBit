from heapq import heappush, heappop

class Solution:
	def getMode(self, A):
		h = {}
		for i in A:
			if h.get(i, None) != None:
				h[i] += 1
			else:
				h[i] = 1

		print(list(h))




sol = Solution()
A = [2, 2, 2, 3, 3]
print(sol.getMode(A))

			



