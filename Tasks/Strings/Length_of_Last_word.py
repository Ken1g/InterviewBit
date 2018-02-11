s = "aa"

class Solution:
	def lengthOfLastWord(self, A):
		length = len(A)
		start = length - 1
		word_st = 0
		count = 0
		if len(A) == 0:
			return 0
		while True:
			if start == -1:
				return count
			if word_st == 0:
				if A[start] != ' ':
					word_st = 1
					count += 1
			else:
				if A[start] == ' ':
					return count
				elif start == 0:
					return count + 1
				else:
					count += 1
			start -= 1
				
			

b = Solution()
print(b.lengthOfLastWord(s))
			
			
