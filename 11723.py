# 집합
import sys
input = sys.stdin.readline

S = [0 for i in range(20)]
M = int(input())
for _ in range(M):
    _input = input().strip().split()

    if _input[0]=='add':
        S[int(_input[1])-1] = 1
    elif _input[0]=='remove':
        S[int(_input[1])-1] = 0
    elif _input[0]=='check':
        print(S[int(_input[1])-1])
    elif _input[0]=='toggle':
        S[int(_input[1])-1] = (0 if S[int(_input[1])-1]==1 else 1)
    elif _input[0]=='all':
        S = [1 for i in range(20)]
    elif _input[0]=='empty':
        S = [0 for i in range(20)]