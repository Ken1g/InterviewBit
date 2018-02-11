class Solution:
	def diffPossible(self, A, B):
		i = j = 0
		if len(A) < 2:
			return 0
		while True:
			if j == len(A) or i == len(A):
				break
			if (A[j] - A[i]) == B and i != j:
				return 1
			elif (A[j] - A[i]) < B:
				j += 1
			else:
				i += 1
		return 0		




A = [1, 2, 3]
B = 0
sol = Solution()
print(sol.diffPossible(A, B))
