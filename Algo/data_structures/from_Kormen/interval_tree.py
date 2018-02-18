class interval:
	def __init__(self, a, b):
		self.low = a
		self.high = b

class Node:
	def __init__(self, a, b):
		self.int = interval(a, b)
		self.key = a
		self.left = None
		self.right = None
		self.p = None
		self.color = None

class int_tree:
	def __init__(self):
		A = Node(None, None)
		A.color = 1
		self.nil = A
		self.root = A

	def max_el(self, x):
		if x.left == self.nil:
			if x.right == self.nil:
				return x.int.high
			else:
				return max(x.int.high, self.max_el(x.right))
		elif x.right == self.nil:
				return max(x.int.high, self.max_el(x.left))
		else:
				return max(x.int.high, self.max_el(x.left), self.max_el(x.right))

	def left_rotate(self, x):
		y = x.right
		x.right = y.left

		if y.left != self.nil:
			y.left.p = x
		y.p = x.p
		if x.p == self.nil:
			self.root = y
		elif x == x.p.left:
			x.p.left = y
		else: 
			x.p.right = y
		y.left = x

		x.p = y

	def right_rotate(self, y):
		x = y.left
		y.left = x.right

		if x.right != self.nil:
			x.right.p = y
		x.p = y.p
		if y.p == self.nil:
			self.root = y
		elif y == y.p.right:
			y.p.right = x
		else:
			y.p.left = x
		x.right = y

		y.p = x

	def insert(self, z):
		y = self.nil
		x = self.root
		while x != self.nil:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.p = y
		if y == self.nil:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
		z.left = self.nil
		z.right = self.nil
		z.color = 0
		self.insert_fixup(z)

	def insert_fixup(self, z):
		while z.p.color == 0:
			if z.p == z.p.p.left:
				y = z.p.p.right
				if y.color == 0:
					z.p.color = 1
					y.color = 1
					z.p.p.color = 0
					z = z.p.p
				elif z == z.p.right:
					z = z.p
					self.left_rotate(z)
					z.p.color = 1
					z.p.p.color = 0
					self.right_rotate(z.p.p)
			else :
				y = z.p.p.left
				if y.color == 0:
					z.p.color = 1
					y.color = 1
					z.p.p.color = 0
					z = z.p.p
				elif z == z.p.left:
					z = z.p
					self.right_rotate(z)
					z.p.color = 1
					z.p.p.color = 0
					self.left_rotate(z.p.p)
		self.root.color = 1

	def transplant(self, u, v):
		if u.p == self.nil:
			self.root = v
		elif u == u.p.left:
			u.p.left = v
		else:
			u.p.right = v
		v.p = u.p

	def search(self, x, k):
		if x == self.nil or k == x.key:
			return x
		if k < x.key:
			return self.search(x.left, k)
		else:
			return self.search(x.right, k)

	def iterative_search(self, x, k):
		while x != self.nil or k != x.key:
			if k < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def minimum(self, x):
		while x.left != self.nil:
			x = x.left
		return x

	def maximum(self, x):
		while x.right != self.nil:
			x = x.right
		return x

	def delete(self, z):
		y = z
		y_original_color = y.color
		if z.left == self.nil:
			x = z.right
			self.transplant(z, z.right)
		elif z.right == self.nil:
			x = z.left
			self.transplant(z, z.left)
		else:
			y = self.minimum(z.right)
			x = y.right
			if y.p == z:
				x.p = y
			else:
				self.transplant(y, y.right)
				y.right = z.right
				y.right.p = y
			self.transplant(z, y)
			y.left = z.left
			y.left.p = y
			y.color = z.color

		if y_original_color == 1:
			self.delete_fixup(x)

	def delete_fixup(self, x):
		while x != self.root and x.color == 1:
			if x == x.p.left:
				w = x.p.right
				if w.color == 0:
					w.color = 1
					x.p.color = 0
					self.left_rotate(x.p)
					w = x.p.right
				if w.left.color == 1 and w.right.color == 1:
					w.color = 0
					x = x.p
				elif w.right.color == 1:
					w.left.color = 1
					w.color = 0
					self.right_rotate(w)
					w = x.p.right
					w.color = x.p.color
					x.p.color = 1
					w.right.color = 1
					self.left_rotate(x.p)
					x = self.root
			else:
				w = x.p.left
				if w.color == 0:
					w.color = 1
					x.p.color = 0
					self.right_rotate(x.p)
					w = x.p.left
				if w.right.color == 1 and w.left.color == 1:
					w.color = 0
					x = x.p
				elif w.left.color == 1:
					w.right.color = 1
					w.color = 0
					self.left_rotate(w)
					w = x.p.left
					w.color = x.p.color
					x.p.color = 1
					w.left.color = 1
					self.right_rotate(x.p)
					x = self.root


		x.color = 1

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

	def interval_search(self, i): # O(lg(n))
		x = self.root
		while x != self.nil and ((i.int.low > x.int.high) or (x.int.low > i.int.high)):
			if (x.left != self.nil) and (self.max_el(x.left) >= i.int.low):
				x = x.left
			else:
				x = x.right
		return x


i_tree = int_tree()
A = Node(16, 21)
i_tree.insert(A)
#print(i_tree.root.int.high)
B = Node(25, 30)
i_tree.insert(B)
#print(i_tree.root.right.int.low)
C = Node(8, 9)
i_tree.insert(C)
#print(i_tree.root.left.int.low)
D = Node(0, 1)
print(i_tree.interval_search(D).int.low)


