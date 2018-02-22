class Solution:
	def longestSubsequenceLength(self, A):
		N = len(A)
		if N == 0:
			return 0
		longest_up = [0 for i in range(N)]
		longest_down = [0 for i in range(N)]

		A = list(A)

		longest_up[0] = 1
		for i in range(1, N):
			el = A[i]
			max_len = 0
			max_j = -1
			for j in range(i):
				if A[j] < A[i]:
					if longest_up[j] > max_len:
						max_len = longest_up[j]
						max_i = j
			longest_up[i] = max_len + 1

		A.reverse()
		longest_down[0] = 1
		for i in range(1, N):
			el = A[i]
			max_len = 0
			max_j = -1
			for j in range(i):
				if A[j] < A[i]:
					if longest_down[j] > max_len:
						max_len = longest_down[j]
						max_i = j
			longest_down[i] = max_len + 1
		longest_down.reverse()
		max_len = 0
		for i in range(N):
			pretend = longest_down[i] + longest_up[i] - 1
			if pretend > max_len:
				max_len = pretend

		return max_len









sol = Solution()
A = [8, 6, 3, 4, 2, 1]
print(sol.longestSubsequenceLength(A))
