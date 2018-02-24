class Solution:
	def minDistance(self, A, B):
		la = len(A)
		lb = len(B)
		ans = [[0 for i in range(la + 1)] for j in range(lb + 1)]
		for j in range(la + 1):
			ans[0][j] = j
		for j in range(lb + 1):
			ans[j][0] = j
		for i in range(1, lb + 1):
			for j in range(1, la + 1):
				if B[i - 1] == A[j - 1]:
					ans[i][j] = ans[i - 1][j - 1]
				else:
					ans[i][j] = 1 + min(ans[i][j - 1], ans[i - 1][j], ans[i - 1][j - 1])
		return ans[-1][-1]

