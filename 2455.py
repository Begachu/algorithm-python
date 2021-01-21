# 지능형 기차
MAX = 0
temp = 0
for i in range(4):
    (_out, _in) = list(map(int, input().split(' ')))
    temp -= _out
    temp += _in
    if temp>MAX:
        MAX = temp
print(MAX)