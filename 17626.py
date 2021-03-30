# Four Squares
import math

cnt = [-1 for i in range(50001)]
cnt[0] = 0
def dp(n):
    if cnt[n]!=-1:
        return cnt[n]
    result = n
    _max = int(math.sqrt(n))
    for i in range(_max, 0, -1):
        result = min(result, 1+dp(n-i*i))
    cnt[n] = result
    return cnt[n]
N = int(input())
print(dp(N))