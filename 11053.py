# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)
N = int(input())
A = list(map(int, input().split()))
cnt = [1]*N
_max = -1

def dp(i):
    global _max, cnt, N, A
    if i==N:
        return 0
    for n in range(0, i):
        if A[i]>A[n] and cnt[n]+1>cnt[i]:
            cnt[i] = cnt[n]+1
    return max(cnt[i], dp(i+1))   

print(dp(0))