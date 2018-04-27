class Solution:

	class Double_ended_queue:
		def __init__(self):
			self.elements = []

		def push_end(self, val):
			self.elements.append(val)

		def push_front(self, val):
			self.elements.insert(0, val)

		def pop_end(self):
			return self.elements.pop()

		def pop_front(self):
			return self.elements.pop(0)

		def is_empty(self):
			if self.elements == []:
				return True
			else:
				return False

	def slidingMaximum(self, A, B):
		if B >= len(A):
			return [max(A)]
		ans = []
		queue = self.Double_ended_queue()
		for i in range(len(A)):
			if queue.is_empty():
				queue.push_front(i)
			else:
				while not queue.is_empty() and A[i] > A[queue.elements[-1]]:
					queue.pop_end()
				queue.push_end(i)
			if (i - queue.elements[0]) >= B:
				queue.pop_front()
			if i >= B - 1:
				ans.append(A[queue.elements[0]])
			print(queue.elements)
		return ans


sol = Solution()
print(sol.slidingMaximum([3, -1, 0, 8, 7, 6, -4, 1, 7, 2], 100))



