class Solution:
	def adjacent(self, A):
		ans = [None for i in range(len(A[0]))]
		if len(A[0]) == 0:
			return 0
		ans[0] = max(A[0][0], A[1][0])
		if len(A[0]) == 1:
			return ans[0]
		ans[1] = max(ans[0], max(A[0][1], A[1][1]))
		if len(A[0]) == 2:
			return ans[1]
		for i in range(2, len(A[0])):
			ans[i] = max(ans[i - 1], ans[i - 2] + max(A[0][i], A[1][i]))

		return ans[-1]


sol = Solution()
A = [[1, 2, 3, 4], [2, 3, 4, 5]]
print(sol.adjacent(A))