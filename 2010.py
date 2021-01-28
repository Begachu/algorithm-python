# 플러그
import sys
input = sys.stdin.readline

result = 0
N = int(input())
for i in range(N):
    result += int(input())-1
print(result+1)