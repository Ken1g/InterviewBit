def repeatedNumber(A):
	N = len(A)
        sum1 = N * (N + 1) / 2
        sum2 = N * (N + 1) * (2*N + 1) / 6
        rsum1 = sum(A)
        rsum2 = 0
        for i in range(N):
        	rsum2 += A[i] * A[i]
        S1 = rsum1 - sum1
	print(S1)
        S2 = rsum2 - sum2
	print(S2)
        ans1 = ((S2 /  S1) + S1 ) / 2
        ans2 = ans1 - S1
	ans = []
	ans.append(ans1)
	ans.append(ans2)
        return ans

A = [2, 2]
print(repeatedNumber(A))
