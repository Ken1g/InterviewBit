class Solution:
	def braces(self, A):
		st = Solution.Stack()
		
		for i in A:
			if i == "(" or i == "+" or i == "*" or i == "/" or i == "-":
				st.push(i)
			elif i == ")":
				quant = 0
				while True:
					if st.pop() == "(":
						break
					else:
						quant += 1
				if quant == 0:
					return 1
		return 0

	


	class Stack:
		def __init__(self):
			self.arr = []
		
		def push(self, el):
			self.arr.append(el)
		
		def pop(self):
			return self.arr.pop()
		
		def empty(self):
			if self.arr == []:
				return True
			else:
				return False



A = "(a + b)"
sol = Solution()
print(sol.braces(A))
