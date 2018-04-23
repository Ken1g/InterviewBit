class Solution:
	def findMedianSortedArrays(self, A, B):
		C = []
		k = 0
		j = 0
		for i in range(len(A) + len(B)):
			if k < len(A) and j < len(B):
				if A[k] < B[j]:
					C.append(A[k])
					k += 1
				else:
					C.append(B[j])
					j += 1
			elif k >= len(A):
				C.append(B[j])
				j += 1
			else:
				C.append(A[k])
				k += 1
		return C


sol = Solution()
print(sol.findMedianSortedArrays([1, 4, 5], [2, 3]))
