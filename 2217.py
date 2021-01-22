# 로프
import sys
input = sys.stdin.readline

N = int(input())
use = 0
_max = -1
save = [0]*10001
for i in range(N):
    temp = int(input())
    if _max<temp:
        _max = temp
    save[temp] += 1

result = 0
for i in range(_max, 0, -1):
    use += save[i]
    weight = i*use
    if result<weight:
        result = weight
print(result)
