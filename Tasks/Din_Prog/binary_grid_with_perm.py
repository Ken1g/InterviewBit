class Solution:
	def counting_sort(self, A, R):
		C = [0 for i in range(R + 1)]
		for j in range(len(A)):
			C[A[j]] += 1
		for j in range(len(C) - 2, -1, -1):
			C[j] += C[j + 1]
		for idx, i in enumerate(C):
			C[idx] = C[idx] * idx
		return max(C)
	
	def solve(self, A):
		if len(A) == 0:
			return 0
		R = len(A)
		C = len(A[0])
		B = [[0 for i in range(C)] for j in range(R)]
		for i in range(C):
			for j in range(R):
				if (j - 1) < 0:
					B[j][i] = A[j][i]
				else:
					if A[j][i] == 0:
						B[j][i] = 0
					else:
						B[j][i] = B[j - 1][i] + 1
		ans = []
		for i in range(R):
			ans.append(self.counting_sort(B[i], R))


		return max(ans)





			









sol = Solution()
A = [[1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0]] 
print(sol.solve(A))
