# 회의실 배정
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
_input = []
result = 0
time = 0

for _ in range(N):
    _input.append(list(map(int, input().split())))
_input.sort(key=lambda x: [x[1],x[0]])

for i in _input:
    if i[0]>=time:
        result += 1
        time = i[1]
print(result)