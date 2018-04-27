class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BSTIterator:
	# @param root, a binary search tree's root node
	def __init__(self, root):
		self.inorder_traversal = []
		self.position = 0
		self.inorder(root)

	def inorder(self, ans, current):
		if current.left:
			self.inorder(current.left)
		self.inorder_traversal.append(current.val)
		if current.right:
			self.inorder(current.right)

	# @return a boolean, whether we have a next smallest number
	def hasNext(self):
		if self.position < len(self.inorder_traversal):
			return True
		else:
			return False

	# @return an integer, the next smallest number
	def next(self):
		self.position += 1
		return self.inorder_traversal[self.position - 1]


	# Your BSTIterator will be called like this:
	# i = BSTIterator(root)
	# while i.hasNext(): print i.next(),