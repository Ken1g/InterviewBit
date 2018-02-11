A = 1212441

def is_Palindrome(A):
	A = str(A)
	for i in range(len(A) / 2 + 1):
		if A[i] != A[len(A) - 1 - i]:
			return 0
	return 1
print(is_Palindrome(A))
