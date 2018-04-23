class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	class Queue:
		def __init__(self):
			self.elements = []

		def is_empty(self):
			if self.elements == []:
				return True
			else:
				return False
		
		def enqueue(self, element):
			self.elements.insert(0, element)

		def dequeue(self):
			if self.is_empty != True:
				return self.elements.pop()
			else:
				return None

	def levelOrder(self, A):
		q = Solution.Queue()
		
		q.enqueue((A, 0))
		ans = []
		while not q.is_empty():
			current, level = q.dequeue()
			if len(ans) <= level:
				ans.append([])
			ans[level].append(current.val)
			
			if current.left:
				q.enqueue((current.left, level + 1))
			if current.right:
				q.enqueue((current.right, level + 1))
		
		return ans

sol = Solution()
v_1 = TreeNode(3)
v_2 = TreeNode(9)
v_3 = TreeNode(20)
v_4 = TreeNode(15)
v_5 = TreeNode(7)

v_1.left = v_2
v_1.right = v_3
v_3.left = v_4
v_3.right = v_5
print(sol.levelOrder(v_1))
		








