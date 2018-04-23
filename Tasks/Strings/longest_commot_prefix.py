class Solution:
	def longestCommonPrefix(self, A):
		still_OK = 1
		no = 0
		pref = []
		pos = 0
		while still_OK:
			base = A[0][pos]
			for string in A:
				if len(string) - 1 == pos:
					no = 1 
				if len(string) - 1 < pos or string[pos] != base:
					still_OK = 0
					break
			pos += 1
			if still_OK:
				pref.append(base)
			if no:
				still_OK = 0
		return "".join(pref)

sol = Solution()
print(sol.longestCommonPrefix(["abc", "abcs", "abcd"]))