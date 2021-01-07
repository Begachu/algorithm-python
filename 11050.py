# 이항 계수 1

_input = input().split(' ')

N = int(_input[0])
K = int(_input[1])

_result = 1

for k in range(K):
    _result *= N
    N -= 1

_K = 1
for k in range(K):
    _K *= 1+k

print(_result//_K)