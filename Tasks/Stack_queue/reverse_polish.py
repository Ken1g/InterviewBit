class Solution:
	class Stack:
    		def __init__(self):
        	 	self.items = []

     		def isEmpty(self):
        		return self.items == []

     		def push(self, item):
         		self.items.append(item)

     		def pop(self):
         		return self.items.pop()

     		def peek(self):
         		return self.items[len(self.items)-1]

     		def size(self):
         		return len(self.items)
	
	def evalRPN(self, A):
		st = Solution.Stack()
		for i in A:
			if i != "*" and i != "+" and i != "-" and i != "/":
				st.push(i)
			else:
				a = st.pop()
				b = st.pop()
				if i == "+":
					st.push(a + b)
				elif i == "-":
					st.push(b - a)
				elif i == "*":
					st.push(a * b)
				else:
					st.push(b / a)
		return st.pop()

sol = Solution()
A = [2, 2, "/"]
print(sol.evalRPN(A))
