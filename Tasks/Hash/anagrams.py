class Solution:
	def anagrams(self, A):
		table = {}
		for idx, val in enumerate(A):
			key = 1
			for j in val:
				key *= ord(j)
			if table.get(key, None) != None:
                        	table[key].append(idx + 1)
			else:
				table[key] = []
				table[key].append(idx + 1)
		ans = []
		for j, i in table.items():
			ans.append(i)
		return ans
 			
				




sol = Solution()
A = ['cat', 'dog', 'god', 'tca']
print(sol.anagrams(A))
