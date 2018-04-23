class Solution:
	def merge_sort(self, A, s, f):
		if s != f:
			m = (f + s) // 2
			self.merge_sort(A, s, m)
			self.merge_sort(A, m + 1, f)
			self.merge(A, s, m, f)

	def merge(self, A, s, m, f):
		n_l = m - s + 1
		n_r = f - m
		L = []
		R = []
		for i in range(n_l):
			L.append(A[s + i])
		for i in range(n_r):
			R.append(A[m + i + 1])
		inf = (9999999, 0)
		L.append(inf)
		R.append(inf)
		j = k = 0 
		for i in range(s, f + 1):
			if L[j][0] < R[k][0]:
				A[i] = L[j]
				j += 1
			else:
				A[i] = R[k]
				k += 1

	def solve(self, A):
		z = []
		for idx, i in enumerate(A):
			z.append((i, idx))
		self.merge_sort(z, 0, len(A) - 1)
		
		print(z)





A = [-1, 0, 0, 0, 3]
sol = Solution()
print(sol.solve(A))