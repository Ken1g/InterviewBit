class Solution:
	
	def merge(self, A, st, mid, fin):
		n_l = mid - st + 1
		n_r = fin - mid
		L = []
		R = []
		inf = 9999999999999
		for i in range(n_l):
			L.append(A[st + i])
		for i in range(n_r):
			R.append(A[mid + i + 1])
		L.append((inf, 0))
		R.append((inf, 0))
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



	class Node:
		def __init__(self, a, b):
			self.a = a
			self.b = b
			self.free = b - a + 1
			self.left = None
			self.right = None
			self.height = -1

	def order(self, A, B):
		N = len(A)
		root = self.Node(0, N - 1)
		self.tree_creator(root)
		zipped = list(zip(A, B))
		self.merge_sort(zipped, 0, len(A) - 1)
		ans = [-1 for j in range(N)]
		for (h, pos) in zipped:
			self.put_height(ans, root, h, pos)
		return ans

	def put_height(self, ans, node, h, pos):
		node.free -= 1
		if node.a == node.b:
			ans[node.a] = h
			
		elif pos < node.left.free:
			self.put_height(ans, node.left, h, pos)
		else:
			self.put_height(ans, node.right, h, pos - node.left.free)



	def tree_creator(self, seg):
		a = seg.a
		b = seg.b
		seg.left = self.Node(a, (a + b) // 2)
		if seg.left.a < seg.left.b:
			self.tree_creator(seg.left)
		seg.right = self.Node((a + b) // 2 + 1, b)
		if seg.right.a < seg.right.b:
			self.tree_creator(seg.right)



sol = Solution()
A = [5, 3, 2, 6, 1, 4]
B = [0, 1, 2, 0, 3, 2]
print(sol.order(A, B)) 
