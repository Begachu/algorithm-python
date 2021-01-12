# 평범한 배낭
import sys
input = sys.stdin.readline
SAVE = [[] for i in range(100)]
stuff = []

_input = input().split(' ')
N = int(_input[0])
M = int(_input[1])
temp = 0
for n in range(N):
    _input = list(map(int, input().split(' ')))
    if M>=_input[0]:
        SAVE[0].append(_input[1])
    else:
        temp -= 1
    stuff.append(_input)

N += temp

for n in range(N):
    _temp_stuff = stuff.copy()
    _temp_stuff.remove(stuff[n])
    m = stuff[n][0]
    for k in range(N-1):
        best = [0,0]
        for i in _temp_stuff:
            if m+i[0]<=M:
                if i[1]>best[1]:
                    best = i
            else:
                _temp_stuff.remove(i)
        if best!=[0,0]:
            _temp_stuff.remove(best)
        result = SAVE[k][n]+best[1]
        m += best[0]
        SAVE[k+1].append(result)

print(sorted(SAVE[N-1],reverse=True)[0])
