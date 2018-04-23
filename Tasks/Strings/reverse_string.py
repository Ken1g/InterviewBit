class Solution:
	def reverseWords(self, A):
		L = len(A)
		word_start = 0
		word = []
		result = []
		for i in range(len(A) - 1, -1, - 1):
			if A[i] != " ":
				word_start = 1
			if word_start:
				if A[i] == " ":
					word_start = 0
					string = "".join(word)
					for j in range(len(string) - 1, -1, -1):
						result.append(string[j])
					result.append(" ")
				else:
					word.append(A[i])
		return "".join(result)
				
		
		
		





A = "the sky is blue"
sol = Solution()
print(sol.reverseWords(A))
