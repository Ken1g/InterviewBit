str = '000'

N = len(str)
summ = []
S = 0
for i in range(N):
	if str[i] == '1':
		S -= 1
	else:
		S += 1
	summ.append(S)
	if S == -1:
		S = 0
max_el = max(summ)
ans = []
if max_el == -1:
	print(ans)
	exit 
i = 0
while summ[i] != max_el:
	 i += 1
start = 0
for j in range(i, -1, -1):
	if summ[j] == -1:
		start = j + 1
		break
ans.append(start + 1)
ans.append(i + 1)
print(ans)	 
	
