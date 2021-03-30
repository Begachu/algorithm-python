# 패션왕 신해빈
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dic = dict()
    N = int(input())
    for n in range(N):
        _input = input().strip().split()
        if _input[1] not in dic:
            dic[_input[1]] = 0
        dic[_input[1]] += 1
    result = 1
    for key in dic:
        result *= dic[key]+1
    result -= 1
    print(result)