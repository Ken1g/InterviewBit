class Solution:
	# @param A : string
	# @return a list of list of strings
	def partition(self, A):
		ans = []
		size_of_first = 1
		self.recursive_partition(ans, [], A)
		return ans

	def recursive_partition(self, ans, current, string):
		if string == "":
			ans.append(current)
		else:
			for i in range(len(string)):
				new_current = current[:]
				to_add = string[:(i + 1)]
				remind = string[(i + 1):]
				if self.is_palindrom(to_add):
					new_current.append(to_add)
					self.recursive_partition(ans, new_current, remind)

	def is_palindrom(self, A):
		ans = True
		for i in range(len(A) // 2 + 1):
			if A[i] != A[-1 - i]:
				ans = False
		return ans


sol = Solution()
print(sol.partition("wwwq"))

