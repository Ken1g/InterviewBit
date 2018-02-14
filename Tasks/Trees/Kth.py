class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def kthsmallest(self, A, B):
		seq = []
		found = 0
		self.inorder(seq, A, B, found)
		return(seq[B - 1])

		
				
	def inorder(self, seq, cur, B, found):
		if not found:
			if cur.left:
				self.inorder(seq, cur.left, B, found)
		seq.append(cur.val)
		if len(seq) >= B:
			found = 1
		if not found:
			if cur.right:
				self.inorder(seq, cur.right, B, found)
		









sol = Solution()
n_1 = TreeNode(4)
n_2 = TreeNode(3)
n_3 = TreeNode(7)
n_4 = TreeNode(1)
n_5 = TreeNode(6)
n_6 = TreeNode(8)
n_7 = TreeNode(2)
n_8 = TreeNode(5)
n_1.left = n_2
n_1.right = n_3
n_2.left = n_4
n_3.left = n_5
n_3.right = n_6
n_4.right = n_7
n_5.left = n_8
print(sol.kthsmallest(n_1, 7))