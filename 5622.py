# 다이얼
import sys
input = sys.stdin.readline

_str = list(input().rstrip())
time = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
result = 0
for i in _str:
    result += time[ord(i)-ord('A')]
print(result)