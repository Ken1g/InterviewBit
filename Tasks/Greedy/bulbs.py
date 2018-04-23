class Solution:
	def bulbs(self, A):
		ans = 0
		for idx, el in enumerate(A):
			state = (A[idx] + ans % 2) % 2
			if state == 0:
				ans += 1

		return ans 









sol = Solution()
A = [1, 0]
print(sol.bulbs(A))