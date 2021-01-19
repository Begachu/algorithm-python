# 소수
SAVE = [-1]*10001
SAVE[0] = 0
SAVE[1] = 0
M, N = int(input()), int(input())
result = 0
_min = -1
temp = 2
index = SAVE[temp:].index(-1)+temp
while index<=N:
    SAVE[index] = 1
    if index>=M:
        if _min==-1:
            _min = index
        result += index
    for i in range(index*2, 10001, index):
        SAVE[i] = 0
    temp = index+1
    if -1 in SAVE[temp:]:
        index = SAVE[temp:].index(-1)+temp
    else:
        index = 10001
if _min==-1:
    print(-1)
else:
    print(result)
    print(_min)