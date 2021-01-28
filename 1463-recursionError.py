# 1로 만들기
import sys
sys.setrecursionlimit(10000)
cnt = [-1]*1000000
cnt[0] = 0
cnt[1] = 1
cnt[2] = 1

def dp(n):
    global cnt
    if cnt[n-1]!=-1:
        return cnt[n-1]
    temp = dp(n-1)+1
    if n%3==0:
        cnt[n-1] = min(dp(n//3)+1,temp)
    elif n%2==0:
        cnt[n-1] = min(dp(n//2)+1,temp)
    else:
        cnt[n-1] = temp
    return cnt[n-1]

print(dp(int(input())))