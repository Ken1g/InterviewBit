class Solution:
	def solve(self, A, B, C):
		i = 0
		j = 0
		k = 0
		ans = 9999999999999
		while True:
			if (i == len(A)) or (j == len(B)) or (k == len(C)):
				break
			curr = max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])
			if curr < ans:
				ans = curr			
			if min(A[i], B[j], C[k]) == A[i]:	
				i += 1
			elif min(A[i], B[j], C[k]) == B[j]:
				j += 1
			else:
				k += 1
		return ans

sol = Solution()
A = [1, 4, 5, 8, 10]
B = [6, 9, 15]
C = [2, 3, 6, 6]
print(sol.solve(A, B, C))
			
				
