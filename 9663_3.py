# N-Queen (9663)

N = int(input())
R = None
C = None
result = 0

def btk(r, c, n):
	global R, C, N, result

	if r==N:
		return
	if c==N:
		return btk(r+1, 0, n)
	if R[r]!=-1:
		return btk(r+1, 0, n)
	if C[c]!=-1:
		return btk(r, c+1, n)
	
	for i in range(N):
		if R[i]!=-1:
			temp = R[i]
			_i = abs(r-i)
			if c-_i>=0:
				if C[c-_i]==temp:
					return btk(r, c+1, n)
			if c+_i<N:
				if C[c+_i]==temp:
					return btk(r, c+1, n)
	n += 1
	if n==N:
		result += 1
	else:
		R[r] = n
		C[c] = n
		btk(r+1, 0, n)
		R[r] = -1
		C[c] = -1
	n -= 1
	return btk(r, c+1, n)

if N==1:
	print(1)
else:
	R = [-1]*N
	C = [-1]*N
	btk(0, 0, 0)
	print(result)
