class Solution:
	def numTrees(self, A):
		ans = [0 for i in range(A + 1)]
		if A == 0:
			return 0
		elif A == 1:
			return 1
		elif A == 2:
			return 2
		ans[0] = 1
		ans[1] = 1
		ans[2] = 2

		for i in range(3, A + 1):
			for j in range(1, i + 1):
				ans[i] += ans[i - j] * ans[j - 1]

		return ans[-1]	








sol = Solution()
print(sol.numTrees(4))