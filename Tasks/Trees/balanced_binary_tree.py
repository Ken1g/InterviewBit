class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
	def isBalanced(self, A):
		ans, height = self.rec(A)
		return ans


	def rec(self, A):
		if A.left == None and A.right == None:
			return 1, 1
		if A.left == None:
			l_b, l_h = 1, 0
		else:
			l_b, l_h = self.rec(A.left)
		if A.right == None:
			r_b, r_h = 1, 0
		else:
			r_b, r_h = self.rec(A.right)


		d = max(l_h, r_h) + 1
		print("node ", A.val, l_h, r_h)
		if (l_b == 1) and (r_b == 1) and (abs(l_h - r_h) <= 1):
			return 1, d
		else:
			return 0, d




sol = Solution()
n_1 = TreeNode(1)
n_2 = TreeNode(2)
n_3 = TreeNode(3)
n_4 = TreeNode(4)
n_5 = TreeNode(5)
n_6 = TreeNode(6)
n_7 = TreeNode(7)
n_8 = TreeNode(8)
n_9 = TreeNode(9)
n_10 = TreeNode(10)
n_11 = TreeNode(11)
n_12 = TreeNode(12)
n_1.left = n_2
n_1.right = n_3
n_2.left = n_4
n_2.right = n_5
n_3.left = n_6
n_4.left = n_7
n_5.right = n_8
n_6.left = n_9
n_6.right = n_10
n_7.right = n_11
n_8.left = n_12
print(sol.isBalanced(n_1))


