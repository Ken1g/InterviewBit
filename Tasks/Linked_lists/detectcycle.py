class ListNode:
        def __init__(self, x):
                self.val = x
                self.next = None

class Solution:
        def detectCycle(self, A):
		was = {}
		while True:
			if A == None:
				return None
			else:
				if was.get(A, None) == True:
					return A
				else:
					was[A] = True
			A = A.next




sol = Solution()
A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(5)
A.next.next.next = A

st = sol.detectCycle(A)
print st.val
