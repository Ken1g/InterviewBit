class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def mergeKLists(self, A):
		import heapq

		p_q = []	
		for root in A:
			p_q.append((root.val, root))
		heapq.heapify(p_q)
		start_root = heapq.heappop(p_q)[1]
		if start_root.next:
			heapq.heappush(p_q, (start_root.next.val, start_root.next))
		prev_Node = start_root
		while p_q != []:
			next_Node = heapq.heappop(p_q)[1]
			if next_Node.next:
				heapq.heappush(p_q, (next_Node.next.val, next_Node.next))
			prev_Node.next = next_Node
			prev_Node = next_Node
		
		return start_root



sol = Solution()
A = ListNode(10)
B = ListNode(14)
C = ListNode(28)
D = ListNode(32)
E = ListNode(33)



ans = sol.mergeKLists([A, D, E, B, C])
while ans:
	print(ans.val)
	ans = ans.next



				


