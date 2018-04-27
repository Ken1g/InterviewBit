class Solution:
	def minWindow(self, A, B):
		ht = {}
		for i in B:
			if ht.get(i, None) == None:
				ht[i] = 1
			else:
				ht[i] += 1
		i = 0
		j = 0
		k = 0
		if len(A) == 0 or len(B) == 0:
			return ""
		to_find = len(B)
		positions = []
		while True:
			if ht.get(A[k], None) != None:
				ht[A[k]] -= 1
				break
			k += 1
			if k == len(A):
				return ""
		to_find -= 1
		i = k
		j = k + 1
		while to_find != 0:	
			if ht.get(A[j], None) != None:
				ht[A[j]] -= 1
				positions.append(j)
				if ht[A[j]] >= 0:
					to_find -= 1
			j += 1
			if j == len(A):
				return ""
		ans = [i, j]
		while j != len(A):
			if to_find == 0:
				if (j - i) < (ans[1] - ans[0]):
					ans = [i, j]
				ht[A[i]] += 1
				if ht[A[i]] > 0:
					to_find += 1
				if positions == []:
					break
				i = positions.pop(0)
			else:
				if ht.get(A[j], None) != None:
					ht[A[j]] -= 1
					positions.append(j)
					if ht[A[j]] >= 0:
						to_find -= 1
				j += 1
		while positions != [] and to_find == 0:
			if (j - i) < (ans[1] - ans[0]):
				ans = [i, j]
			i = positions.pop(0)
			ht[A[i]] += 1
			if ht[A[i]] > 0:
				to_find += 1


		return A[ans[0] : ans[1]]

sol = Solution()
print(sol.minWindow("cavc", "cv"))