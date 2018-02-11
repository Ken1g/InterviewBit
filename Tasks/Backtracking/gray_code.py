class Solution:
	def grayCode(self, A):
		ans = []
		self.create(A, ans)
		return ans
			
	
	def create(self, n, ans):
		if n == 1:
			ans.append(0)
			ans.append(1)
		else:
			self.create(n - 1, ans)
			for i in range(len(ans) - 1, -1, -1):
				ans.append(ans[i])
			for i in range(len(ans) // 2):
				ans[i + len(ans) // 2] += 2 ** (n - 1)
	

sol = Solution()
A = 2
print(sol.grayCode(A))	
