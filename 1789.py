# 수들의 합 (1789)
S = int(input())
A = [i for i in range(1, 100000)]
for i in range(1, len(A)):
	A[i] += A[i-1]

i = 0
while S-A[i]>=0:
	i += 1

if S-A[i]==0:
	print(i+1)
else:
	print(i)
