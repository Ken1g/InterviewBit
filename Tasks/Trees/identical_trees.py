class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	class Queue:
	        def __init__(self):
	                self.items = []

	        def isEmpty(self):
	                return self.items == []

	        def enqueue(self, item):
	                self.items.insert(0, item)

	        def dequeue(self):
	                return self.items.pop()

	        def size(self):
	                return len(self.items)



	def isSameTree(self, A, B):
		if A == None:
			if B == None:
				return 1
			else: 
				return 0
		l1 = l2 = r1 = r2 = TreeNode(0)	
		cur_1 = A
		cur_2 = B
		q1 = self.Queue()
		q2 = self.Queue()
		q1.enqueue(A)
		q2.enqueue(B)
		ident = 1
		while q1.isEmpty() == 0 or q2.isEmpty() == 0:
			if (q1.isEmpty == 1):
				return 0
			if (q2.isEmpty == 1):
				return 0	
			el1 = q1.dequeue()
			el2 = q2.dequeue()
			if el1.val != el2.val:
				ident = 0
				break
			if el1.left != None:
				l1 = el1.left
				q1.enqueue(el1.left)
			if el1.right != None:
				r1 = el1.right
				q1.enqueue(el1.right)
			if el2.left != None:
				l2 = el2.left
				q2.enqueue(el2.left)
			if el2.right != None:
				r2 = el2.right
				q2.enqueue(el2.right)
			if (l1.val != l2.val) or (r1.val != r2.val):
				ident = 0
				break
		return ident


sol = Solution()
n_1 = TreeNode(0)
n_2 = TreeNode(0)
print(sol.isSameTree(n_1, n_2))


