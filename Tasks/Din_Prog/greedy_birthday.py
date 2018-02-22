class Solution:
	def solve(self, A, B):
		R = A
		to_be_considered = []
		idxes = []
		minimum = 999999999
		for idx, i in enumerate(B):
			if i < minimum:
				minimum = i
				to_be_considered.append(i)
				idxes.append(idx)

		N = R // (to_be_considered[-1])
		ans = [idxes[-1] for i in range(N)]

		sum = N * to_be_considered[-1]
		for i in range(N):
			for jdx, j in enumerate(to_be_considered):
				if sum + (j - to_be_considered[-1]) <= R:
					sum += (j - to_be_considered[-1])
					ans[i] = idxes[jdx]
					break

		return ans









sol = Solution()
B = [6, 8, 5, 4, 7]
A = 11
print(sol.solve(A, B))



