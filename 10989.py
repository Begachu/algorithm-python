# 수 정렬하기 3
import sys

N = int(sys.stdin.readline())
array = [0 for i in range(10000+1)]

for i in range(N):
    array[int(sys.stdin.readline())] += 1

for i in range(1, 10000+1):
    for j in range(array[i]):
        print(i)