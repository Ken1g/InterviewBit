class Solution:
	def colorful(self, A):
		prod = {}

		st = str(A)
		length = len(st)

		for i in range(1, length + 1):
				m = 1
				for k in range(i, length + 1):
					interesting = (A % 10 ** (m + i - 1)) // (10 ** (m - 1))
					k = self.product(i, interesting)
					if prod.get(k, None) == True:
						return 0
					else:
						prod[k] = True
					m += 1
		return 1

	def product(self, length, A):
		pr = 1
		for i in range(1, length + 1):
			pr *= (A % 10 ** i) // (10 ** (i - 1))

		return pr


sol = Solution()
A = 12
print(sol.colorful(A))
		
