class Solution:

	class BinHeap:

		def __init__(self):
			root = 999999999
			# -1, -1 for indicies
			self.heapList = [[root, -1, -1]]
			self.currentSize = 0

		def percUp(self,i):
			root = 999999999
			while i // 2 > 0:
				if self.heapList[i][0] > self.heapList[i // 2][0]:
					tmp = self.heapList[i // 2]
					self.heapList[i // 2] = self.heapList[i]
					self.heapList[i] = tmp
				i = i // 2

		def insert(self,k):
			self.heapList.append(k)
			self.currentSize = self.currentSize + 1
			self.percUp(self.currentSize)	

		def percDown(self,i):
			while (i * 2) <= self.currentSize:
				mc = self.maxChild(i)
				if self.heapList[i][0] < self.heapList[mc][0]:
					tmp = self.heapList[i]
					self.heapList[i] = self.heapList[mc]
					self.heapList[mc] = tmp
				i = mc

		def maxChild(self,i):
			if i * 2 + 1 > self.currentSize:
				return i * 2
			else:
				if self.heapList[i * 2][0] > self.heapList[i * 2 + 1][0]:
					return i * 2
				else:
					return i * 2 + 1
	
		def delMax(self):
			retval = self.heapList[1]
			self.heapList[1] = self.heapList[self.currentSize]
			self.currentSize = self.currentSize - 1
			self.heapList.pop()
			self.percDown(1)
			return retval

	def solve(self, A, B):
		used = {}
		A.sort()
		B.sort()
		bh = Solution.BinHeap()
		N = len(A)
		n_a = N - 1
		n_b = N - 1
		el = []
		el.append(A[n_a] + B[n_b])
		el.append(n_a)
		el.append(n_b)
		key = n_a * N + n_b
		used[key] = True
		ans = []
		ans.append(el[0])
		while len(ans) != N:
			if used.get((n_a - 1) * N + n_b, None) == None:
				bh.insert([A[n_a - 1] + B[n_b], n_a - 1, n_b])
				used[(n_a - 1) * N + n_b] = True
			if used.get(n_a * N + (n_b - 1), None) == None:
				bh.insert([A[n_a] + B[n_b - 1], n_a, n_b - 1])
				used[n_a * N + (n_b - 1)] = True
			el = bh.delMax()
			n_a = el[1]
			n_b = el[2]
			ans.append(el[0])
		return ans

				
sol = Solution()
A = [-3, -2, -1, 0, 1, 2, 3]
B = [-3, -2, -1, 0, 1, 2, 3]





A = [ 36, 27, -35, 43, -15, 36, 42, -1, -29, 12, -23, 40, 9, 13, -24, -10, -24, 22, -14, -39, 18, 17, -21, 32, -20, 12, -27, 17, -15, -21, -48, -28, 8, 19, 17, 43, 6, -39, -8, -21, 23, -29, -31, 34, -13, 48, -26, -35, 20, -37, -24, 41, 30, 6, 23, 12, 20, 46, 31, -45, -25, 34, -23, -14, -45, -4, -21, -37, 7, -26, 45, 32, -5, -36, 17, -16, 14, -7, 0, 37, -42, 26, 28 ]
B = [ 38, 34, -47, 1, 4, 49, -18, 10, 26, 18, -11, -38, -24, 36, 44, -11, 45, 20, -16, 28, 17, -49, 47, -48, -33, 42, 2, 6, -49, 30, 36, -9, 15, 39, -6, -31, -10, -21, -19, -33, 47, 21, 31, 25, -41, -23, 17, 6, 47, 3, 36, 15, -44, 33, -31, -26, -22, 21, -18, -21, -47, -31, 20, 18, -42, -35, -10, -1, 46, -27, -32, -5, -4, 1, -29, 5, 29, 38, 14, -22, -9, 0, 43 ]

#A = [42, 43, 43, 45, 46, 48]
#B = [46, 46, 47, 47, 47, 49]


print(sol.solve(A, B))
