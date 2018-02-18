class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def lca(self, A, B, C):
		result_1 = self.find(A, B, [])
		result_2 = self.find(A, C, [])
		if result_2 == None or result_1 == None:
			return -1
		i = 0
		while True:
			if result_1[i] == result_2[i]:
				i += 1
				if i == len(result_1) or i == len(result_2):
					return result_1[i - 1]
			else:
				return result_1[i - 1]


	def find(self, current, wanted, path):
		new_path = path[:]
		new_path.append(current.val)
		if current.val == wanted:
			return new_path
		else:
			if current.left:
				maybe = self.find(current.left, wanted, new_path)
				if maybe:
					return maybe
			if current.right:
				maybe = self.find(current.right, wanted, new_path)
				if maybe:
					return maybe







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
a5.right = a8
B = 7
C = 8
print(sol.lca(A, B, C))
