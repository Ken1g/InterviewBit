class Solution:
	def strStr(self, haystack, needle):
		if needle == "" or haystack == "":
			return -1
		in_needle = 0
		pos = 0
		if len(haystack) < len(needle):
			return -1
		for i in range(len(haystack) - len(needle) + 1):
			string = ""
			for k in range(i, i + len(needle)):
				string += haystack[k]
			if string == needle:
				return i
		return -1


haystack = "bbbbb"
needle = "ere"

sol = Solution()
print(sol.strStr(haystack, needle))
