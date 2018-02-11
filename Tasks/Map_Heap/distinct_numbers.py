class Solution:

	def dNums(self, A, B):
		l = len(A)
		ans = []
		if B > l:
			return ans
		quant = 0
		ht = {}
		for i in range(0, B):
			if ht.get(A[i], None) == None:
				ht[A[i]] = 1
				quant += 1
			else:
				ht[A[i]] += 1
		ans.append(quant)
		for i in range(B, l):
			if ht.get(A[i - B], None) == 1:
				ht[A[i - B]] = None
				quant -= 1
			else:
				ht[A[i - B]] -= 1
			if ht.get(A[i], None) == None:
				ht[A[i]] = 1
				quant += 1
			else:
				ht[A[i]] += 1
			ans.append(quant)
		return ans

sol = Solution()
A = [1, 2, 1, 3, 4, 3]
B = 3
print(sol.dNums(A, B))