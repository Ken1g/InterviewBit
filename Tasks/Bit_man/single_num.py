class Solution:
	def singleNumber(self, A):
		ans = 0
		for i in A:
			ans ^= i
		return ans
		

A = [1, 2, 3, 3, 1]
sol = Solution()
print(sol.singleNumber(A))
