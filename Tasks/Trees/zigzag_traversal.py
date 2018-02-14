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

	def zigzagLevelOrder(self, A):
		nodes = self.Queue()
		levels = self.Queue()
		nodes.enqueue(A)
		levels.enqueue(0)
		cur_level = -1
		ans = []
		i = 0
		while not nodes.isEmpty():
			current = nodes.look()
			level = levels.look()
			if cur_level != level:
				cur_level = level
				i = not i
				z = 0
				add = []
				while (len(levels.items) > z) and (levels.items[z] == cur_level):
					add.append(nodes.items[z].val)
					z += 1
				if i == 0:
					ans.append(add)
				else:
					add.reverse()
					ans.append(add)
			nodes.dequeue()
			levels.dequeue()
			if current.left:
				nodes.enqueue(current.left)
				levels.enqueue(level + 1)
			if current.right:
				nodes.enqueue(current.right)
				levels.enqueue(level + 1)
		return ans


sol = Solution()
n_1 = TreeNode(3)
n_2 = TreeNode(9)
n_3 = TreeNode(20)
n_4 = TreeNode(15)
n_5 = TreeNode(7)n_5 = TreeNode(7)
n_1.left = n_2
n_1.left = n_2
n_1.right = n_3
n_3.left = n_4
n_3.right = n_5
n_6 = TreeNode(100)
n_5.left = n_6
print(sol.zigzagLevelOrder(n_1))
