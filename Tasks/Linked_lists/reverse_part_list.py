class ListNode:
        def __init__(self, x):
                self.val = x
                self.next = None

class Solution:
        def reverseBetween(self, A, m, n):
        	i = 0
		inner = 0
		add_list = []
		head = A
		start1 = A
		finish1 = None
		while True:
			if A == None:
				break
			i += 1
			if i == m - 1:
				start1 = A
			elif i == m:
				inner = 1
			elif i == n + 1:
				inner = 0
				finish1 = A
			if inner:
				add_list.append(A.val)
			A = A.next

		add = ListNode(add_list[-1])
		start2 = add
		for i in range(len(add_list) - 2, -1, -1):
			add.next = ListNode(add_list[i])
			add = add.next
		finish2 = add
		start1.next = start2
		finish2.next = finish1
		
		if m != 1:
			return head
		else:
			return head.next
			
			
				
				
A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
A.next.next.next = ListNode(4)

sol = Solution()
st = sol.reverseBetween(A, 2, 2)
while st != None:
	print st.val
	st = st.next

