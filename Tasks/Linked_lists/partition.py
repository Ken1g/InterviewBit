class ListNode:
        def __init__(self, x):
                self.val = x
                self.next = None

class Solution:
        def partition(self, A, B):
		l1 = ListNode(0)
		st1 = l1
		l2 = ListNode(0)
		st2 = l2
		while True:
			if A == None:
				st1.next = l2.next
				return l1.next					
			if A.val < B:
				st1.next = ListNode(A.val)
				st1 = st1.next
			else:
				st2.next = ListNode(A.val)
				st2 = st2.next
				
			A = A.next		
		
	


sol = Solution()
A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(5)
A.next.next.next = ListNode(3)

st = sol.partition(A, 4)
while st != None:
	print st.val
	st = st.next

