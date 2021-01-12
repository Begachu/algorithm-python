# 마인크래프트
import sys
input = sys.stdin.readline
world = []
_min = 256
_max = 0


# get input data, N:x, M:y, B:number of block
(N, M, B) = list(map(int, input().split(' ')))
for n in range(N):
    _input = list(map(int, input().split(' ')))
    for m in range(M):
        B += _input[m]
        if _min>_input[m]:
            _min = _input[m]
        if _max<_input[m]:
            _max = _input[m]
    world.append(_input)

S = 256*N*M*2
B = B//(N*M)
if B>=_max:
    B = _max
H = B
_s = 0

while B>=_min:
    _s = 0
    
    for i in range(N):
        for j in range(M):
            temp = world[i][j]
            if B==temp:
                continue
            elif B>temp:
                _s += B-temp
            else:
                _s += 2*(temp-B)
    if S>_s:
        H = B
        S = _s
    if S<_s:
        break
    B -= 1

print(S, H)