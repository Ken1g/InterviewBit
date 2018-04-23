class Solution:
	def generate(self, A):
		ans = []
		ans.append([1])
		for i in range(1, A):
			ans.append([1])
			for j in range(i - 1):
				ans[i].append(ans[i - 1][j] + ans[i - 1][j + 1])
			ans[i].append(1)

		return ans









sol = Solution()
A = 3
print(sol.generate(A))