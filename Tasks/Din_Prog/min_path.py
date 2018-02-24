class Solution:
	def minPathSum(self, A):
		if len(A) == 0:
			return 0
		R = len(A)
		C = len(A[0])

		ans = [[None for _ in range(C)] for _ in range(R)]
		sum = 0
		for i in range(R):
			ans[i][0] = A[i][0] + sum
			sum += A[i][0]
		sum = 0
		for i in range(C):
			ans[0][i] = A[0][i] + sum
			sum += A[0][i]

		for i in range(R):
			for j in range(C):
				if ans[i][j] == None:
					ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + A[i][j]

		return ans

sol = Solution()
A = [[1, 3, 2], [4, 3, 1], [5, 6, 1]]
print(sol.minPathSum(A))