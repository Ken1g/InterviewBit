A = 177214

def primesum(A):
	is_prime = []
	for i in range(0, A + 1):
		is_prime.append(bool(1))
	is_prime[0] = bool(0)
	is_prime[1] = bool(0) 
	for i in range(0, A + 1):
		if is_prime[i] == 1:
			s = 2 * i
			while s <= A:
				is_prime[s] = bool(0)
				s += i
	for i in range(1, A + 1):
		if is_prime[i] == 1 and is_prime[A - i] == 1:
			return(i, A - i)

print(primesum(A))
		
