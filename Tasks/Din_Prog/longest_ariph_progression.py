class Solution:
	def solve(self, A):
		N = len(A)
		table = {}
		for idx, el in enumerate(A):
			for j in range(idx, N):
				table[(el, j)] = idx

		if N == 0:
			return 0
		elif N == 1:
			return 1
		dp = [[None for i in range(N)] for j in range(N)]
		for i in range(N):
			for j in range(i + 1, N):
				dp[i][j] = 2
				need = 2 * A[i] - A[j]
				pos = -1
				pos = table.get((need, i - 1))
				if pos != None:
					dp[i][j] = max(dp[i][j], dp[pos][i] + 1)

		maximum = 0
		for ar in dp:
			for el in ar:
				if (el):
					if el > maximum:
						maximum = el 

		return maximum


		




sol = Solution()
A = [1]
print(sol.solve(A))