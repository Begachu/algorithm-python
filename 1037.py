# 약수
N = int(input())
_input = list(map(int, input().split(' ')))
_input.sort()
print(_input[0]*_input[N-1])