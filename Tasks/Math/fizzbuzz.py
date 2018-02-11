A = 16

def fizzBuzz(A):
	ans = []
	for i in range(A):
		ans.append(i + 1)
	for i in range(2, A, 3):
		ans[i] = "Fizz"
	for i in range(4, A, 5):
		if ans[i] == "Fizz":
			ans[i] = "FizzBuzz"
		else:
			ans[i] = "Buzz"
	
	return ans

print(fizzBuzz(A))
	
