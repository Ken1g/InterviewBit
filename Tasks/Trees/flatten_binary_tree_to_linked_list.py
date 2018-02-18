class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def flatten(self, A):
		result = []
		self.order_traversal(result, A)
		for i in range(len(result) - 1):
			result[i].left = None
			result[i].right = result[i + 1]
		return(result[0])


	def order_traversal(self, result, current):
		result.append(current)
		if current.left:
			self.order_traversal(result, current.left)
		if current.right:
			self.order_traversal(result, current.right)

 















sol = Solution()
A = TreeNode(3)
a1 = TreeNode(5)
a2 = TreeNode(1)
a3 = TreeNode(6)
a4 = TreeNode(2)
a5 = TreeNode(0)
a6 = TreeNode(8)
a7 = TreeNode(7)
a8 = TreeNode(4)
A.left = a1
A.right = a2
a1.left = a3
a1.right = a4
a2.left = a5
a2.right = a6
a4.left = a7
a4.right = a8
print(sol.flatten(A))


