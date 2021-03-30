# DSLR
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    visited = [False]*10000
    (A, B) = list(map(int, input().split()))
    visited[A] = True
    queue = deque([(A, '')])
    while len(queue)>0:
        (N, S) = queue.popleft()
        n = str(N)
        while len(n)<4:
            n = '0'+n
        temp = (N*2)%10000
        if not visited[temp]:
            queue.append((temp, S+"D"))
            visited[temp] = True
            if temp==B:
                print(S+"D")
                break
        temp = (N-1 if N>0 else 9999)
        if not visited[temp]:
            queue.append((temp, S+"S"))
            visited[temp] = True
            if temp==B:
                print(S+"S")
                break
        temp = int(n[1:]+n[0])
        if not visited[temp]:
            queue.append((temp, S+"L"))
            visited[temp] = True
            if temp==B:
                print(S+"L")
                break
        temp = int(n[3]+n[:3])
        if not visited[temp]:
            queue.append((temp, S+"R"))
            visited[temp] = True
            if temp==B:
                print(S+"R")
                break