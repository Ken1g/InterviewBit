A = ["This"]
B = 10


def fullJustify(A, B):
	i = 0
	ans = []
	last = 0
	while True:
		if i == len(A):
			break
		pack_len = len(A[i])
		j = i
		while pack_len <= B:
			j += 1
			if j == len(A):
				last = 1
				break
			pack_len += len(A[j]) + 1
		j -= 1
		num = j - i
		free = B
		add = 0
		for k in range(i, j + 1, 1):
			free -= len(A[k])
		if num != 0:
			full = free / num
		if num != 0:
			add = free % num
		string = []
		whitespaces = []
		whitespaces.append(0)
		for l in range(add):
			whitespaces.append(full + 1)
		for l in range(num - add):
			whitespaces.append(full)
		if last == 1:
			for k in range(i, j + 1):
				string += A[k]
				if k != j:
					string += ' '
			string += ' ' * (B - len(string))
			ans.append(string)
			return ans
		else:
			for k in range(i, j + 1):
				string += whitespaces[k - i] * ' '
				string += A[k]
		if num == 0:
			string += free * ' '
		ans.append(string)
		i = j + 1
	return ans
	
print(fullJustify(A, B))	
