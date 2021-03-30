# 절댓값 힙
import heapq
import sys
input = sys.stdin.readline

N = int(input())
h = []
for n in range(N):
    x = int(input())
    if x==0:
        if len(h)==0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x), x))