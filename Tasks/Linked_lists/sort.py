class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def sortList(self, A):
		N = 1
		current = A
		while current.next:
			N += 1
			self.merge_sort(A, None, N)

	def merge_sort(self, start, parent_of_start, number_of_nodes):
		parent_second_half = start
		i = 1
		while i < N // 2:
			parent_second_half = parent_second_half.next
			second_half = parent_second_half.next
			i += 1
		self.merge_sort(start, parent_of_start N // 2)
		self.merge_sort(second_half, parent_second_half, N - N // 2)
		self.merge(start, second_half, N // 2, N - N // 2)

	def merge(self, first, second, fN, sN):


