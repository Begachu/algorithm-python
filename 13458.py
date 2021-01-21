# 시험 감독
import sys
input = sys.stdin.readline

N = int(input())
candidate = list(map(int, input().split(' ')))
(main_observer, sub_observer) = list(map(int, input().split(' ')))
result = 0

for n in range(N):
    result += 1
    candidate[n] -= main_observer
    if candidate[n]>0:
        result += candidate[n]//sub_observer
        if candidate[n]%sub_observer!=0:
            result += 1

print(result)