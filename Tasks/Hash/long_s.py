class Solution:
	def lengthOfLongestSubstring(self, A):
		start = 0
		table = {}
		length = 0
		max_length = 0
		for idx, ch in enumerate(A):
			key = ord(ch)
			if table.get(key, None) != None:
				if table[key] >= start:
					if length > max_length:
						max_length = length
					start = table[key] + 1
					length = idx - start + 1
					table[key] = idx
				else:
					table[key] = idx
					length += 1
			else:
				table[key] = idx
				length += 1
		if length > max_length:
                                        max_length = length
		return max_length	

sol = Solution()
A = "bbbbbb" 
print(sol.lengthOfLongestSubstring(A))
