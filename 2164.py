# 카드2
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque(x+1 for x in range(N))

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())