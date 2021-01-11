# 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline

_input = list(map(int, input().split(' ')))
cnt = deque([i for i in range(1,_input[0]+1)])
result = []

while len(cnt)>0:
    for i in range(_input[1]-1):
        cnt.append(cnt.popleft())
    result.append(str(cnt.popleft()))

print('<'+', '.join(result)+'>')