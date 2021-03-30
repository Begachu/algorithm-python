# 이중 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    heap = []
    for n in range(N):
        (m, i) = input().split()
        if m=='I':
            heapq.heappush(heap, int(i))
        elif m=='D':
            if len(heap)!=0:
                if int(i)==-1:
                    heapq.heappop(heap)
                else:
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
    if len(heap)==0:
        print("EMPTY")
    else:
        print(heapq.nlargest(1, heap)[0], heap[0])