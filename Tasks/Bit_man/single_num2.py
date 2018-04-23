class Solution:
	def singleNumber(self, A):
		bits = [0 for i in range(32)]

		for i in A: 
			mask = 1
			for j in range(32):
				res = (i & mask) >> j
				if res == 1:
					bits[j] = (bits[j] + 1) % 3
				mask = mask << 1
		res = 0
		for i in range(len(bits)):
			if bits[i]:
				res += 2 ** i
		return res	

sol = Solution()
print(sol.singleNumber([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]))
