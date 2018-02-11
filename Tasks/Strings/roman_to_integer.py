class Solution:
	def romanToInt(self, A):
		integers = []
		ans = 0
		for i in A:
			if i == 'I':
				integers.append(1)
			elif i == 'V':
				integers.append(5)
			elif i == 'X':
				integers.append(10)
			elif i == 'L':
				integers.append(50)
			elif i == 'C':
				integers.append(100)
			elif i == 'D':
				integers.append(500)
			elif i == 'M':
				integers.append(1000)
		integers.append(-1)
		for i in range(len(A)):
			if integers[i] < integers[i + 1]:
				ans -= integers[i]
			else:
				ans += integers[i]
		return ans
			
	
sol = Solution()
A = 'DCC'
print(sol.romanToInt(A))
