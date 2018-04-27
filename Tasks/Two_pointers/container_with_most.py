class Solution:
	def maxArea(self, A):
		if len(A) <= 1:
			return 0
		raising_seq = []
		st = 1
		for idx, i in enumerate(A):
			if i >= st:
				raising_seq.append((idx, i))
				st = i
		st = -1
		decreasing_seq = []
		for j in range(len(A) - 1, -1, -1):
			if A[j] >= st: 
				decreasing_seq.append((j, A[j]))
				st = A[j]

		i = 0
		j = 0

		ans = 0
		while raising_seq[i][0] < decreasing_seq[j][0]:
			res = (decreasing_seq[j][0] - raising_seq[i][0]) * min(decreasing_seq[j][1], raising_seq[i][1])
			if res > ans:
				ans = res
			if decreasing_seq[j][1] > raising_seq[i][1]:
				i += 1
			else:
				j += 1

		return ans







sol = Solution()
print(sol.maxArea([1000, 2]))