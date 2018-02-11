class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution():

	def inorderTraversal(self, A):
		curr = A
		ans = []	
		st = Stack()
		popper = 0
		while True:
			if popper == 0:
				st.push(curr)
				if curr.right != None:
					st.push("r")
				if curr.left != None:
					curr = curr.left
				else:
					popper = 1
			else:
				if st.isEmpty() == True:
					return ans
				el = st.pop()
				if el == "r":
					el = st.pop()
					curr = el.right
					ans.append(el.val)
					popper = 0
				else:
					ans.append(el.val)
		
				
			
sol = Solution()
C = TreeNode(3)
B = TreeNode(2)
B.left = C
A = TreeNode(1)
A.right = B
print(sol.inorderTraversal(A)) 
