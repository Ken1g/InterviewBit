A = 678
B = 534

def Euq(A, B):	
	while A != 0 and B != 0:
		if A > B:
			A %= B
		else:
			B %= A
	return(A + B)

print(Euq(A, B))

