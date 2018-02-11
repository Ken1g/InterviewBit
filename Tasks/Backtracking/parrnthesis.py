class Solution:
	def generateParenthesis(self, A):
		ans = []
		start = ""
		self.create(ans, 0, 0, start, A)
		
		return ans

	def create(self, ans, n, m, start, A):
		if len(start) == 2 * A:
			ans.append(start)
		else:
			if n == A:
				new_start = start + ")"
				self.create(ans, n, m + 1, new_start, A)
			else:
				new_start = start + "("
				self.create(ans, n + 1, m, new_start, A)
				if m < n:
					new_start = start + ")"
					self.create(ans, n, m + 1, new_start, A)

			
		







sol = Solution()
A = 3
print(sol.generateParenthesis(A))
