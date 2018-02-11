class Solution:
	def intersect(self, A, B):
		i = 0
		j = 0
		ans = []
		while True:
			if (i == len(A)) or (j == len(B)):
				break
			if A[i] == B[j]:
				ans.append(A[i])
				i += 1
				j += 1
			elif A[i] > B[j]:
				j += 1
			else:
				i += 1
		return ans
				




sol = Solution()
A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 3, 5]
print(sol.intersect(A, B))

