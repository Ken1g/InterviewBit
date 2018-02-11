class Solution:
	def qsort(self, A, p, r):
        	if p < r:
                	q = self.partition(A, p, r)
                	self.qsort(A, p, q - 1)
                	self.qsort(A, q, r)


	def partition(self, A, p, r):
        	pivot = A[r]
        	i = p - 1
        	for j in range(p, r):
                	if A[j] <= pivot:
                        	i += 1
                        	A[i], A[j] = A[j], A[i]
        	A[r], A[i + 1] = A[i + 1], A[r]

        	return i + 1

	def findMinXor(self, A):
		self.qsort(A, 0, len(A) - 1)
		min = 999999999999999
		for i in range(len(A) - 1):
			if (A[i] ^ A[i + 1]) < min:
				min = A[i] ^ A[i + 1]
		return min
	





A = [12, 4, 6, 2]
sol = Solution()
print(sol.findMinXor(A))
