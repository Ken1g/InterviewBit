class Solution:
    	def atoi(self, A):	
		# 48 to 57
		start = 0
		while ord(A[start]) > 57 or ord(A[start]) < 48:
			if ord(A[start]) == 45 or ord(A[start]) == 43:
				if start == len(A) - 1:
					return 0
				if ord(A[start + 1]) <= 57 and ord(A[start + 1]) >= 48:
					start += 1
					continue
				else:
					return 0
			if ord(A[start]) != 32:
				return 0
			start += 1
		end = start
		while 48 <= ord(A[end]) <= 57:
			end += 1
			if end == len(A):
				break
		dec = 0
		ans = 0
		for i in range(end - 1, start - 1, -1):
			ans += ((ord(A[i]) - 48) * (10 ** dec))
			dec += 1	
		if start != 0:
			if A[start - 1] == '-':
				ans = -ans
		INT_MAX = 2147483647	
		INT_MIN = - INT_MAX - 1
		if ans > INT_MAX:
			return INT_MAX
		elif ans < INT_MIN:
			return INT_MIN
		else:
			return ans
		

sol = Solution()
print(sol.atoi(" +1000"))

