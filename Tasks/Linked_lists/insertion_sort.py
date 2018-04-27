class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def insertionSortList(self, A):
		current = A
		#A = self.swap_nodes(A, 3, 0)
		length = 0
		while current:
			length += 1
			current = current.next
		current = A.next

		for i in range(1, length):

			check = A
			#print("iteration", i)
			while check:
			#	print(check.val)
				check = check.next
			
			j = 0
			internal = A
			while current.val > internal.val:
				internal = internal.next
				j += 1
			current = current.next
			A = self.insert_nodes(A, i, j)

		return A

	def insert_nodes(self, A, i, j):
		if i == j:
			return A
		else:
			cur = A
			for k in range(i + 1):
				if k == i:
					first = cur
				if k == j:
					second = cur
				if k == i - 1:
					prev_first = cur
				if k == j - 1:
					prev_second = cur
				cur = cur.next
			if j == 0:
				prev_first.next = first.next
				first.next = second
				return first
			else:
				prev_first.next = first.next
				prev_second.next = first
				first.next = second
				return A

		


sol = Solution()
A = ListNode(6)
B = ListNode(5)
C = ListNode(4)
D = ListNode(3)
E = ListNode(2)
F = ListNode(1)
C.next = D
B.next = C
A.next = B  
D.next = E
E.next = F
current = sol.insertionSortList(A)
while current:
	print(current.val)
	current = current.next