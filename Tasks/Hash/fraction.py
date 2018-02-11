class Solution:
	def fractionToDecimal(self, numerator, denominator):
		table = {}
		ans = ""
		fraction = ""
		if (numerator < 0) ^ (denominator < 0):
			ans += "-"
			numerator = abs(numerator)
			denominator = abs(denominator)
		whole = numerator // denominator 
		remainder = numerator % denominator
		if remainder == 0:
			return str(whole)
		else:
			ans += str(whole) + "."
		pos = 0
		while True:
			remainder *= 10
			whole = remainder // denominator
			remainder %= denominator
			#print("///", whole, remainder)
			if remainder == 0:
				fraction += str(whole)
				ans += fraction
				return ans
			if table.get(remainder, None) != None:
				pos = table[remainder]
				if fraction[pos] != str(whole):
					fraction += str(whole)
					pos += 1
				fraction = fraction[:pos] + '(' + fraction[pos:] + ")"
				ans += fraction
				return ans
			else:
				table[remainder] = pos
				fraction += str(whole)
			pos += 1





sol = Solution()
numerator = 87
denominator = 22
print(sol.fractionToDecimal(numerator, denominator))
