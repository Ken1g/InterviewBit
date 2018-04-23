class Solution:
	def getRow(self, A):
		ans = [1]
		for i in range(1, A + 1):
			new = []
			new.append(1)
			for j in range(i - 1):
				new.append(ans[j] + ans[j + 1])
			new.append(1)
			ans = new[:]

		return ans

sol = Solution()
print(sol.getRow(3))