# 빠른 A+B
import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    _input = input().split(' ')
    print(int(_input[0])+int(_input[1]))