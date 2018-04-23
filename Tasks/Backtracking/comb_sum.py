class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
	def combinationSum(self, A, B):
		ans = []
		A.sort()
		new_A = []
		ht = {}
		for i in A:
			if ht.get(i, None) == None:
				new_A.append(i)
				ht[i] = True
		current = []

		self.exc(B, new_A, 0, ans, current)

		return list(reversed(ans))
		



	def exc(self, sum, values, idx, ans, current):
		if idx  == len(values) - 1:
			new_current = current[:]
			if sum % values[idx] == 0:
				for j in range(sum // values[idx]):
					new_current.append(values[idx])
				ans.append(new_current)
		else:
			j = 0
			while j * values[idx] <= sum:
				new_current = current[:]
				for i in range(j):
					new_current.append(values[idx])
				self.exc(sum - j * values[idx], values, idx + 1, ans, new_current)
				j += 1


sol = Solution()
print(sol.combinationSum([1, 6, 8, 8, 10, 11, 16], 28))