# 스택 수열
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
result = []
stack = deque()
last = 1

while len(result)<N*2:
    _input = int(input())
    while last<=_input:
        stack.appendleft(last)
        result.append("+")
        last += 1
    if stack[0]==_input:
        stack.popleft()
        result.append("-")
    else:
        print("NO")
        result = []
        break

for i in result:
    print(i)
    