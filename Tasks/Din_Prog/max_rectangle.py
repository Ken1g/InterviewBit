class Solution:
	class Stack:
		def __init__(self):
			self.arr = []
		
		def push(self, el):
			self.arr.append(el)
		
		def pop(self):
			if self.empty():
				return None
			return self.arr.pop()

		def peek(self):
			if self.arr == []:
				return None
			return self.arr[-1]
		
		def empty(self):
			if self.arr == []:
				return True
			else:
				return False

	def largestRectangleArea(self, A):
		max_recktangle = 0
		st = self.Stack()
		for i in range(len(A)):
			if st.empty() or A[i] >= A[st.peek()]:
				st.push(i)
			if A[i] < A[st.peek()]:
				while (st.empty() == False) and (A[st.peek()] > A[i]):
					pretend = st.pop()
					h = A[pretend]
					R = i
					L = st.peek()
					if L == None:
						L = -1
					max_recktangle = max(max_recktangle, (R - L - 1) * h)
				st.push(i)
		i = len(A)
		while (st.empty() == 0):
			pretend = st.pop()
			h = A[pretend]
			R = i
			L = st.peek()
			if L == None:
				L = -1
			max_recktangle = max(max_recktangle, (R - L - 1) * h)
		
		return max_recktangle








	def maximalRectangle(self, A):
		if len(A) == 0:
			return 0
		R = len(A)
		C = len(A[0])
		B = [[0 for i in range(C)] for j in range(R)]
		for i in range(C):
			for j in range(R):
				if (j - 1) < 0:
					B[j][i] = A[j][i]
				else:
					if A[j][i] == 0:
						B[j][i] = 0
					else:
						B[j][i] = B[j - 1][i] + 1

		ans = []
		for i in range(R):
			ans.append(self.largestRectangleArea(B[i]))

		return max(ans)






sol = Solution()
A = [[1, 1, 0], [1, 1, 0], [0, 1, 0]] 
print(sol.maximalRectangle(A))