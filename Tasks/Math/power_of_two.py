class Solution:
	def Eu(self, A, B):
		while A != 0 or B != 0:
			if A > B:
				A %= B
			else:
				B %= A
			return(A + B)

	def isPower(self, A):
		start = A
		arr = []
		ht = {}
		if A == 1:
			return 1
		while start != 1:
			j = 2
			while True:
				if start % j == 0:
					arr.append(j)
					if ht.get(j, None) == None:
						ht[j] = 1
					else:
						ht[j] += 1
					start //= j
					break
				j += 1
		factors = list(ht.values())
		A = factors[0]
		for i in factors:
			B = i
			A = self.Eu(A, B)
		if A == 1:
			return 0
		else:
			return 1


				
		

sol = Solution()
print(sol.isPower(102401))


