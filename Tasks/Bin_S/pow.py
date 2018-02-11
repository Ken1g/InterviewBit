def pow(x, n, d):
	if n == 0:
        	return 1 % d
        temp = pow(x, n / 2, d)
        return (temp * temp) % d if n % 2 == 0 else (x * temp * temp) % d
        

print(pow(2, 4, 10000000))
			
			
