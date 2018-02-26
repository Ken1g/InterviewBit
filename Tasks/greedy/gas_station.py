class Solution:
	def canCompleteCircuit(self, A, B):
		R = [(A[i] - B[i]) for i in range(len(A))]
		if len(R) == 0:
			return -1
		if len(R) == 1:
			if R[0] >= 0:
				return 0
			else:
				return -1
		for i in range(len(R)):
			R.append(R[i])
		start = 0
		finish = 0 
		path_length = 0
		sum = 0
		while path_length < len(A):
			if start >= len(A):
				return -1

			sum += R[finish]
			if sum < 0:
				start += 1
				path_length -= 1
				if path_length < 0:
					finish += 1
					sum = 0
					path_length = 0
				else:
					sum -= R[finish]
					sum -= R[start - 1]
			else:
				finish += 1
				path_length += 1
		return start






sol = Solution()
G = [4, 1, 2]
C = [2, 2, 3]
print(sol.canCompleteCircuit(G, C))