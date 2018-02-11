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
  	

	def prevSmaller(self, arr):
		st = Solution.Stack()
		ans = []
		for i in arr:
			while True:
				if st.isEmpty():
					ans.append(-1)
					break
				elif st.peek() < i:
					ans.append(st.peek())
					break
				else:
					st.pop()
			st.push(i)
		
		return ans

sol = Solution()
A = [1]
print(sol.prevSmaller(A))
		
		
