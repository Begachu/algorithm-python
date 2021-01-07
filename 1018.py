# 체스판 다시 칠하기

WANT = ['W','B','W','B','W','B','W','B']

_input = input().split(' ')

N = int(_input[0])
M = int(_input[1])
borad = []
result = 64

for i in range(N):
    borad.append(list(input()))

for y in range(N-7):
    for x in range(M-7):
        _try = 0
        _try_R = 0

        for i in range(8):
            _temp = borad[y+i][x:x+8]
            _compare = 0
            _compare_R = 0

            for k in range(8):
                if _temp[k]!=WANT[k]:
                    _compare += 1
                else:
                    _compare_R += 1

            if i%2==0:
                _try += _compare
                _try_R += _compare_R
            else:
                _try += _compare_R
                _try_R += _compare

        if _try<result:
            result = _try
        if _try_R<result:
            result = _try_R

print(result)
