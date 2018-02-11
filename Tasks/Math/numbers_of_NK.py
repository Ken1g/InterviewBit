A = [0, 1, 3, 4, 6, 7]
B = 4
C = 59172

def solve(A, B, C):
	if len(A) == 0:
		return 0
	s = str(C)
	l = len(s)
	digits = []
	for i in range(l):
		digits.append(int(s[i]))
	if B > l:
		return 0
	elif B < l:
		if A[0] != 0:
			return len(A) ** B
		else:
			if B == 1:
				return len(A)
			else:
				return len(A) ** B - len(A) ** (B - 1)
	else:
		dp = []
		dp.append(0)
		for i in range(1, B + 1):
			dp.append(dp[i - 1] * len(A))
			exist = 1
			for k in range(i - 1):
				if digits[k] not in A:
					exist = 0
			#########################
			if exist:
				add = 0
				for m in A:
					if m < digits[i - 1]:
						if (m != 0) or (i != 1) or (B == 1):
							add += 1
				dp[i] += add
		return dp[B]
				
			
			
			

print(solve(A, B, C))
