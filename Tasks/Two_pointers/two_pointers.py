class Solution:
	def maxone(self, A, B):
		answer = []
		if len(A) == 0:
			return answer
		i = 0
		j = 0
		diff = 0
		max = 0
		if A[0] == 0:
			diff = 1
		while True:
			if diff > B:
				if (j - i) > max:
					max = j - i
					ans = []
					ans.append(i)
					ans.append(j)
				i += 1
				if A[i - 1] == 0:
					diff -= 1
			else:
				j += 1
				if j == len(A):		
					if (j - i) > max:
						ans = []
						ans.append(i)
						ans.append(j)
					break
				if A[j] == 0:
					diff += 1
		for i in range(ans[0], ans[1]):
			answer.append(i)
		
		return answer
			
				





A = [0, 1, 1, 1]
M = 0
sol = Solution()
print(sol.maxone(A, M))
