class Solution:

	class Node:
		def __init__(self, val, name):
			self.val = val
			self.leftChild = None
			self.rightChild = None
			self.name = name
		def get(self):
			return self.val

		def set(self, val):
			self.val = val

		def getChildren(self):
			children = []
			if(self.leftChild != None):
				children.append(self.leftChild)
			if(self.rightChild != None):
				children.append(self.rightChild)
			return children

	class BST:
		def __init__(self):
			self.root = None

		def setRoot(self, val, name):
			self.root = Solution.Node(val, name)

		def insert(self, val, name):
			if (self.root is None):
				self.setRoot(val, name)
			else:
				self.insertNode(self.root, val, name)

		def insertNode(self, currentNode, val, name):
			if (val <= currentNode.val):
				if (currentNode.leftChild):
					self.insertNode(currentNode.leftChild, val, name)
				else:
					currentNode.leftChild = Solution.Node(val, name)
			elif(val > currentNode.val):
				if(currentNode.rightChild):
					self.insertNode(currentNode.rightChild, val, name)
				else:
					currentNode.rightChild = Solution.Node(val, name)

		def find(self, val, name):
			return self.findNode(self.root, val, name)

		def findNode(self, currentNode, val, name):
			if (currentNode is None):
				return False
			elif (val == currentNode.val):
				if name == currentNode.name:
					return True
				else:
					return self.findNode(currentNode.leftChild, val, name)
			elif (val < currentNode.val):
				return self.findNode(currentNode.leftChild, val, name)
			else:
				return self.findNode(currentNode.rightChild, val, name)


	def solve(self, A, B):
		g_words = A.split('_')
		words = []
		ans = []
		for el in B:
			words.append(el.split('_'))
		bstree =  Solution.BST()
		for el in g_words:
			name = el
			key = 0
			for j in el:
				key += ord(j)
			bstree.insert(key, name)
		for idx, rev in enumerate(words):
			q = 0
			for w in rev:
				key = 0
				for j in w:
					key += ord(j)
				if (bstree.find(key, w)):
					q += 1
			ans.append([q, idx])
		self.merge_sort(ans, 0, len(ans) - 1)	
		final_ans = []
		for j in range(len(ans) - 1, -1, -1):
			final_ans.append(ans[j][1])
			
		return final_ans


	def merge(self, A, st, mid, fin):
		import numpy as np

		n_l = mid - st + 1
		n_r = fin - mid
		L = []
		R = []
		for i in range(n_l):
			L.append(A[st + i])
		for i in range(n_r):
			R.append(A[mid + i + 1])
		L.append([np.inf, 0])
		R.append([np.inf, 0])
		j = k = 0
		for i in range(st, fin + 1):
			if L[j][0] < R[k][0]:
				A[i] = L[j]
				j += 1
			else:
				A[i] = R[k]
				k += 1


	def merge_sort(self, A, st, fin):
		if st != fin:
			mid = (st + fin) // 2
			self.merge_sort(A, st, mid)
			self.merge_sort(A, mid + 1, fin)
			self.merge(A, st, mid, fin)

				
			


sol = Solution()
A = "cool_ice_wifi"
B = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
print(sol.solve(A, B))
