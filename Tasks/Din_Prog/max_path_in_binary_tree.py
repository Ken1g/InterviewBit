class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def maxPathSum(self, A):
		maximum = [-9999999999999]

		self.to_bottom(A, maximum)
		return maximum[0]
		



	def to_bottom(self, node, maximum):
		if node.left == None and node.right == None:
			return node.val
		res_l = 0
		res_r = 0
		if node.left:
			res_l = self.to_bottom(node.left, maximum)
		if node.right:
			res_r = self.to_bottom(node.right, maximum)
		ans = max(res_l, res_r)
		maximum[0] = max(res_l + res_r + node.val, maximum[0], node.val)
		return ans + node.val




sol = Solution()
n_1 = TreeNode(-100)
n_2 = TreeNode(-200)
n_3 = TreeNode(-300)
n_4 = TreeNode(-400)
n_1.left = n_2
n_2.right = n_4	
n_2.left = n_3	
print(sol.maxPathSum(n_1))

