# 벽장문의 이동
import sys
input = sys.stdin.readline

N = int(input())
_open = list(map(int, input().split()))
T = int(input())
cnt = [-1]*T

for t in range(T):
    cnt[t] = int(input())

def dp(o1, o2, n):
    global N, T, cnt
    if T==n:
        return [0]
    
    temp = cnt[n]
    if temp==o1 or temp==o2:
        return [min(dp(o1, o2, n+1))]
    
    result1 = abs(temp-o1)
    result2 = abs(temp-o2)

    o2_1 = o2 + (result2+1 if o1<o2 and o2<temp else (-result2-1 if o1>o2 and o2>temp else 0))
    o1_2 = o1 + (result1+1 if o2<o1 and o1<temp else (-result1-1 if o2>o1 and o1>temp else 0))

    result = []
    if o2_1<=N and o2_1>0:
        result.append(result1+min(dp(temp, o2_1, n+1)))
    if o1_2<=N and o1_2>0:
        result.append(result2+min(dp(temp, o1_2, n+1)))
    return result

print(min(dp(_open[0], _open[1], 0)))