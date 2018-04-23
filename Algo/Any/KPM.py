def compute_prefix_function(P):
	m = len(P)
	pi = []
	pi.append(0)
	k = 0
	for q in range(1, m):
		while k > 0 and P[k] != P[q]:
			k = pi[k - 1]
		if P[k] == P[q]:
			k += 1
		pi.append(k)
	return pi

def KMP(T, P):
	ans = []
	n = len(T)
	m = len(P)
	pi = compute_prefix_function(P)
	q = 0
	for i in range(n):
		while q > 0 and P[q] != T[i]:
			q = pi[q - 1]
		if P[q] == T[i]:
			q += 1
		if q == m:
			ans.append(i - m + 1)
			q = pi[q - 1]
	return ans

print(KMP("abcabcd", "ab"))
print(KMP("abcdabca", "ab"))