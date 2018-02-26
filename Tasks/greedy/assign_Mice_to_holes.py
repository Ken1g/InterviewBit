class Solution:
	def mice(self, A, B):
		A.sort()
		B.sort()
		ans = 0
		for i in range(len(A)):
			pretend = abs(A[i] - B[i])
			if pretend > ans:
				ans = pretend
		return ans







A = [4, -4, 2]
B = [4, 0, 5]
sol = Solution()
print(sol.mice(A, B))
