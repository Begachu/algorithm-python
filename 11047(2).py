# 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = [0 for n in range(N)]

for n in range(N):
    coin[n] = int(input())

