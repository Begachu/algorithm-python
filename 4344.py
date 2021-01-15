# 평균은 넘겠지
import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    _input = list(map(int, input().split(' ')))
    avg = sum(_input[1:])/_input[0]
    temp = 0
    for j in range(_input[0]):
        if _input[j+1]>avg:
            temp += 1
    print("%.3f" %(100*temp/_input[0])+"%")