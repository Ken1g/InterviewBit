class Solution:
	def majorityElement(self, A):
		import math
		n = math.floor(len(A) / 2)
		table = {}
		for i in A:
			if table.get(i, None) == None:
				table[i] = 1
			else:
				table[i] += 1
			if table[i] > n:
					return i




sol = Solution()
A = [2, 1, 2]
print(sol.majorityElement(A))