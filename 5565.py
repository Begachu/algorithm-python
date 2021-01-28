# 영수증
import sys
input = sys.stdin.readline
result = int(input())
for i in range(9):
    result -= int(input())
print(result)