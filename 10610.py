# 30
number = [0]*10
N = list(input())
N.sort(reverse=True)
no_zero = (False if N[len(N)-1]=='0' else True)
_sum = 0
for index in N:
    _sum +=int(index)
if no_zero:
    print(-1)
elif _sum%3!=0:
    print(-1)
else:
    print(''.join(N))
