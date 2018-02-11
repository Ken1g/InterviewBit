class ListNode:
	def __init__(self, x):
        	self.val = x
        	self.next = None

class Solution:
	def deleteDuplicates(self, A):
		head = A
		while True:
			if A == None:
				return head
			if A.next == None:
				return head
			while A.next.val == A.val:
				if A.next.next == None:
					A.next = None
					break
				A.next = A.next.next
			A = A.next


sol = Solution()
A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(2)
A.next.next.next = ListNode(2)
print(sol.deleteDuplicates(A).val)
