class Solution:
	def HammingDistance(self, A):
		ans = 0
		mask = 1
		for i in range(32):
			zeros = 0
			ones = 0
			for element in A:
				if (element & mask):
					ones += 1
				else:
					zeros += 1
			ans += 2 * ones * zeros
			mask <<= 1

		return ans % 1000000007
			
			
sol = Solution()
array = [2, 4, 6]
print(sol.HammingDistance(array))
