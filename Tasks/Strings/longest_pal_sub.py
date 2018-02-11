class Solution:
	def longestPalindrome(self, A):
		l = len(A)
		max1 = 0
		pos1 = 0
		for i in range(l):
			same = 1
			length = 1
			k = 1
			while same == 1:
				if (i + k) <= (l - 1) and (i - k) >= 0:
			#		print A[i - k], A[i + k]
					if A[i + k] == A[i - k]:
						length += 2
						k += 1
					else:
						same = 0
				else:
					same = 0
			if length > max1:
				max1 = length
				pos1 = i
				
		max2 = 0
		pos2 = 0
		for i in range(l - 1):
			same = 1
			length = 0
			k = 0
			while same == 1:		
				if (i + k + 1) <= (l - 1) and (i - k) >= 0:
			#		print A[i - k], A[i + k + 1]
					if A[i - k] == A[i + k + 1]:
						length += 2
						k += 1
					else:
						same = 0
				else:
					same = 0
			if length > max2:
				max2 = length
				pos2 = i
		typ = 0
		if max1 > max2:
			typ = 1
		elif max2 > max1:
			typ = 2
		else:
			if pos1 < pos2:
				typ = 1
			else:
				typ = 2
		ans = ""
		if typ == 1:
			for i in range(pos1 - max1 // 2, pos1 + max1 // 2 + 1):
				ans += A[i]
		else:
			for i in range(pos2 - max2 // 2 + 1, pos2 + max2 // 2 + 1):
				ans += A[i]
		return ans





A = 'abb'
sol = Solution()
print(sol.longestPalindrome(A))
