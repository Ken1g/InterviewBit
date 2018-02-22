class Solution:

	def solve(self, A):
		if len(A) == 0:
			return 0
		R = len(A)
		C = len(A[0])
		pre = [[0 for i in range(C)] for j in range(R)]

		
		for i in range(R):
			for j in range(C):
				if (i - 1) >= 0 and (j - 1) >= 0:
					pre[i][j] = A[i][j] + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1]
				elif (i - 1) >= 0 and (j - 1) < 0:
					pre[i][j] = A[i][j] + pre[i - 1][j]
				elif (j - 1) >= 0 and (i - 1) < 0:
					pre[i][j] = A[i][j] + pre[i][j - 1]
				else:
					pre[i][j] = A[i][j]
		ans = 0
		for r1 in range(R):
			for r2 in range(r1, R):
				arr = [0 for i in range(C)]
				for i in range(C):
					if r1 - 1  >= 0:
						arr[i] = pre[r2][i] - pre[r1 - 1][i]
					else:
						arr[i] = pre[r2][i]
				table = {}
				for el in arr:
					pretend = table.get(el, None) 
					if pretend == None:	
						table[el] = 1
						if el == 0:
							ans += 1
					else:
						table[el] += 1
						if el == 0:
							ans += table[0]
						else:
							ans += (table[el] - 1)
						




		return ans







A = [[-8], [8], [-8], [8], [-8]]
sol = Solution()
print(sol.solve(A))	
