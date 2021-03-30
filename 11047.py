# 동전 0
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, K = map(int, input().split())
coin = [0 for n in range(N)]

for n in range(N):
    coin[n] = int(input())

def ga(k, i):
    if i==0:
        return k
    elif k==0:
        return 0
    elif k<coin[i]:
        return ga(k, i-1)
    else:
        return k//coin[i]+ga(k%coin[i], i-1)

print(ga(K, N-1))