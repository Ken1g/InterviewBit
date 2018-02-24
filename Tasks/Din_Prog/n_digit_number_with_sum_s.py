class Solution:
	def solve(self, A, B):
		modulo = 1000000007
		ans = [[0 for i in range(B + 1)] for j in range(A + 1)]
		for i in range(B + 1):
			if i <= 9:
				ans[1][i] = 1
		ans[1][0] = 0

			
		
		for i in range(2, A + 1):
			for j in range(0, B + 1):
				sum_to = 0
				for k in range(j - 9, j + 1):
					if k < 0:
						continue
					else:
						sum_to += ans[i - 1][k]
					ans[i][j] = sum_to
		return ans[-1][-1] % modulo












sol = Solution()
A = 4
B = 2 	
print(sol.solve(A, B))