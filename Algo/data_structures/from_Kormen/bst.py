# All the operations will be complited for the O(h) time, where h stands for the height or the tree

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.p = None

class BST:
	def __init__(self):
		self.root = None
	
	def search(self, x, k):
		if x == None or k == x.key:
			return x
		if k < x.key:
			return self.search(x.left, k)
		else:
			return self.search(x.right, k)

	def iterative_search(self, x, k):
		while x != None or k != x.key:
			if k < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def minimum(self, x):
		while x.left != None:
			x = x.left
		return x

	def maximum(self, x):
		while x.right != None:
			x = x.right
		return x

	def successor(self, x): # return the element after by the key x or None if x the biggest one
		if x.right != None:
			return self.minimum(x.right)
		y = x.p
		while y != None and x == y.right:
			x = y
			y = y.p
		return y

	def predecessor(self, x):
		if x.left != None:
			return self.maximum(x.left)
		y = x.p
		while y != None and x == y.left:
			x = y
			y = y.p
		return y

	def insert(self, z):
		y = None
		x = self.root
		while x != None:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.p = y
		if y == None:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z

	def transplant(self, u, v):
		if u.p == None:
			self.root = v
		elif u == u.p.left:
			u.p.left = v
		else:
			u.p.right = v
		if v != None:
			v.p = u.p
	def delete(self, z):
		if z.left == None:
			self.transplant(z, z.right)
		elif z.right == None:	
			self.transplant(z, z.left)
		else: 
			y = self.minimum(z.right)
			if  y.p != z:
				self.transplant(y, y.right)
				y.right = z.right
				y.right.p = y
			self.transplant(z, y)
			y.left = z.left
			y.left.p = y

	

tree = BST()
A = Node(20)
B = Node(15)
tree.insert(A)
print(tree.search(tree.root, 20).key)
tree.insert(B)
print(tree.search(tree.root, 20).left.key)
C = Node(30)
tree.insert(C)
D = Node(40)
tree.insert(D)
print(tree.predecessor(C).key)
print(tree.successor(C).key)
tree.delete(C)
print(tree.search(tree.root, 30))

