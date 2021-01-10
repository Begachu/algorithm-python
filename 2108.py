# 통계학
import sys
input = sys.stdin.readline

SAVE = [0]*(4000*2+1)
N = int(input())
_avg = 0
_mid = 0
_mode = 0
_mode_amount = 0
_min = 4001
_max = -4001

# get input and compute mode's amount & range
for i in range(N):
    index = int(input())
    _avg += index
    SAVE[index+4000] += 1
    temp = SAVE[index+4000]
    if temp>_mode_amount:
        _mode_amount = temp
    if _min>index:
        _min = index
    if _max<index:
        _max = index


# compute mid
temp = N//2+1
for i in range(8001):
    temp -= SAVE[i]
    if temp<=0:
        _mid = i-4000
        break


# compute mode
_mode = SAVE.index(_mode_amount)
SAVE[_mode] = -1
if _mode_amount in SAVE:
    _mode = SAVE.index(_mode_amount)


print(int(round(_avg/N, 0)))    # avg
print(_mid)                     # mid
print(_mode-4000)                    # mode
print(_max-_min)                # range