class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def invertTree(self, A):
		self.changeTree(A)
		return A
		

	def changeTree(self, A):
		left = A.left
		right = A.right
		A.left = right
		if right:
			self.changeTree(A.right)
		A.right = left
		if left:
			self.changeTree(A.left)








sol = Solution()
n_1 = TreeNode(0)
n_2 = TreeNode(1)
n_3 = TreeNode(2)
n_1.right = n_2
n_1.left = n_3


print(sol.invertTree(n_1).left.val)