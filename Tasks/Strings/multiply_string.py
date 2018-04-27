class Solution:
	def multiply(self, A, B):
		if A == "0" or B == "0":
			return "0"
		for idx, i in enumerate(A):
			if i != "0":
				A = A[idx:]
				break
		for idx, i in enumerate(B):
			if i != "0":
				B = B[idx:]
				break
		to_sum = []
		la = len(A)
		lb = len(B)
		for i in range(lb):
			new = []
			numb = int(B[lb - 1 - i])
			carry = 0
			for j in range(la):
				numa = int(A[la - 1 - j])
				res = numa * numb + carry
				new.append(str(res % 10))
				carry = res // 10
			if carry != 0:
				new.append(str(carry))
			new.reverse()
			for j in range(i):
				new.append("0")
			to_sum.append(new)
		ans = []
		carry = 0
		maxlen = len(to_sum[-1])
		for i in range(maxlen):
			res = 0
			for string in to_sum:
				if len(string) > i:
					add = int(string[-1 - i])
					res += add
			res += carry
			carry = res // 10
			ans.append(str(res % 10))
		if carry != 0:
			ans.append(str(carry))
		ans.reverse()
		if ans == [] or ans[0] == "0":
			ans = ['0']

		return "".join(ans)

sol = Solution()
print(sol.multiply("12345", "0"))





