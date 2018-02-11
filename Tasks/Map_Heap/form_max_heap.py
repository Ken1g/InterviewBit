class Solution:
	def solve(self, A):
		import math

		if (A <= 2):
			return 1
		elif (A == 3):
			return 2
		h = int(math.log(A, 2))
		m = 2 ** h
		p = A - (m - 1)
		if (p >= m / 2):
			L = m - 1
		else:
			L = m - 1 - (m / 2 - p)
		R = A - 1 - L	
		C = int(math.factorial(A - 1) / (math.factorial(R) * math.factorial(L)))
		L = int(L)
		R = int(R)
		ans = ((self.solve(L) * self.solve(R)) * C) % 1000000007
		return int(ans)

		
   

A = 20
sol = Solution()
print(sol.solve(A))
