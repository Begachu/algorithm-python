# 합
N = int(input())
even = N//2
if N%2==0:
    print((N+1)*even)
else:
    print(N*even+N)