class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def buildTree(self, A):
		m, i = self.findMAX(A, 0, len(A))
		root = TreeNode(m)
		self.treecreator(A, 0, i, len(A), root)

		return root

	def treecreator(self, A, st, mid, fn, node):
		m1, i1 = self.findMAX(A, st, mid)
		m2, i2 = self.findMAX(A, mid + 1, fn)
		if m1 != None:
			node.left = TreeNode(m1)
			self.treecreator(A, st, i1, mid, node.left)
		if m2 != None:
			node.right = TreeNode(m2)
			self.treecreator(A, mid + 1, i2, fn, node.right)

	def findMAX(self, A, st, fn):
		if st >= fn:
			return None, None
		m = A[st]
		i = st
		for idx in range(st, fn):
			if A[idx] > m:
				m = A[idx]
				i = idx
		return m, i



sol = Solution()
A = [1, 2, 7, 6, 8, 4, 2, 3, 0]
root = sol.buildTree(A)
def printtree(A):
	print(A.val)
	if A.left:
		printtree(A.left)
	if A.right:
		printtree(A.right)

printtree(root)


	 
