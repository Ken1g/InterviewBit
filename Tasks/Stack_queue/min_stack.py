class MinStack:
    	def __init__(self):
		self.el = []
		self.m = []

	# @param x, an integer
    	def push(self, x):
        	self.el.append(x)
		if len(self.m) == 0:
			self.m.append(len(self.el) - 1)
		elif x < self.el[self.m[-1]]:
			self.m.append(len(self.el) - 1) 
		print(self.m)

    	# @return nothing
    	def pop(self):
		if (len(self.el) == 0):
			return 
		if (len(self.el) - 1) == self.m[-1]:
			self.m.pop()
        	return(self.el.pop())

    	# @return an integer
    	def top(self):
        	if len(self.el) == 0:
            		return -1  
        	else:
            		return(self.el[len(self.el) - 1])
            
    	# @return an integer
    	def getMin(self):
		if len(self.el) == 0:
			return -1
		return self.el[self.m[-1]]


st = MinStack()
st.push(10)
st.push(9)
print(st.getMin())

