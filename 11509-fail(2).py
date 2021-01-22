# 풍선 맞추기
from collections import deque

save = []
N = int(input())
balloon = list(map(int, input().split(' ')))
save.append(balloon[0]-1)

for i in range(1, N):
    start = 0
    end = len(save)
    _balloon = balloon[i]
    while start<end-1:
        half = (start+end)//2
        temp = save[half]
        if temp==_balloon:
            start = half
            break
        elif temp>_balloon:
            end = half-1
        else:
            start = half+1
    if start<len(save) and save[start]==_balloon:
        save[start] -= 1
    else:
        save.append(_balloon-1)
    save.sort()
print(len(save))