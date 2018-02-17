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

	        def look(self):
	        	if len(self.items) != 0:
	        		return self.items[-1]
	        	else:
	        		return None

	        def size(self):
	                return len(self.items)

	def haspathsum(self, A, B):
		current = [A, A.val]
		q = self.Queue()
		q.enqueue(current)
		while not q.isEmpty():
			current = q.dequeue()
			no_left = 0
			no_right = 0
			if current[0].left:
				q.enqueue([current[0].left, current[1] + current[0].left.val])
			else: no_left = 1
			if current[0].right:
				q.enqueue([current[0].right, current[1] + current[0].right.val])
			else: no_right = 1
			if no_right and no_left:
				if current[1] == B:
					return 1
		return 0







sol = Solution()
n_1 = TreeNode(3)
n_2 = TreeNode(9)
n_3 = TreeNode(20)
n_4 = TreeNode(15)
n_5 = TreeNode(7)
n_1.left = n_2
n_1.right = n_3
n_3.left = n_4
n_3.right = n_5
n_6 = TreeNode(100)
n_5.left = n_6
B = 10

print(sol.haspathsum(n_1, 38))