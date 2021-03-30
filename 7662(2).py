# 이중 우선순위 큐
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    queue = deque()
    for n in range(N):
        (m, i) = input().split()
        if m=='I':
            start = 0
            end = len(queue)
            while start<end:
                half = (start+end)//2
                if queue[half]<int(i):
                    end = half
                elif queue[half]>int(i):
                    start = half + 1
                else:
                    start = half
                    break
            queue.insert(start, int(i))
        else:
            if len(queue)!=0:
                if int(i)==1:
                    queue.popleft()
                else:
                    queue.pop()
    if len(queue)==0:
        print("EMPTY")
    else:
        print(queue[0], queue[len(queue)-1])