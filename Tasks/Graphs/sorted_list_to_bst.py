class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def sortedListToBST(self, A):
		arr = []
		current = A
		while current != None:
			arr.append(current.val)
			current = current.next
		m = self.findMid(arr, 0, len(arr) - 1)
		root = TreeNode(arr[m])
		self.create_tree(root, m, 0, len(arr) - 1, arr)
		return root
		

	def findMid(self, arr, s, f):
		if s > f:
			return None			
		else:
			return (f + s) // 2
		
	def create_tree(self, root, m, start, finish, arr):
		lm = self.findMid(arr, start, m - 1)
		if lm != None:
			root.left = TreeNode(arr[lm])
			self.create_tree(root.left, lm, start, m - 1, arr)
		rm = self.findMid(arr, m + 1, finish)
		if rm:
			root.right = TreeNode(arr[rm])
			self.create_tree(root.right, rm, m + 1, finish, arr)
		

sol = Solution()
n_1 = ListNode(0)
n_2 = ListNode(1)
n_3 = ListNode(2)
n_4 = ListNode(3)
n_1.next = n_2
n_2.next = n_3
n_3.next = n_4
print(sol.sortedListToBST(n_1).right.right.val)





