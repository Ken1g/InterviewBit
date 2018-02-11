A = [1, 5, 7, 8, 1, 1, 1, 6, 4, 1, 5, 6, 7, 9, 0, 4, 5, 6]

def repeatedNumber(A):
	c = []
	n = []
	for idx, i in enumerate(A):
		if i not in n:
			if len(n) < 2:
				n.append(i)
				c.append(1)
			elif len(n) == 2:
				for j in range(1, -1, -1):
					if c[j] == 1:
						del c[j]
						del n[j]
					else:
						c[j] -= 1
		else:
			c[n.index(i)] += 1	
	
	if len(n) == 0:
		return -1
	else:
		corr = len(A) / 3.0
		for k in n:
			ans = 0
			for i in A:
				if i == k:
					ans += 1
			if ans > corr:
				return k
		return -1
					

print(repeatedNumber(A))

	
