class Solution:
	def countAndSay(self, A):
		old = "1"
		if A == 1:
			return old
		for i in range(A - 1):
			curr = old[0]
			quant = 0
			new = ''
			for k in old:
				if k == curr:	
					quant += 1
				else:
					new += str(quant)
					new += curr
					curr = k
					quant = 1
			new += str(quant)
                        new += curr
			old = new
		
		return old
		
A = 1
st = Solution()
print(st.countAndSay(A))
