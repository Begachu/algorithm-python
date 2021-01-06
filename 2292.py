# 벌집

N = int(input())-1

_temp = 0

while True:
    N -= _temp
    if N <= 0:
        break
    else:
        _temp += 6

if _temp == 0:
    print(1)
else:
    print(_temp//6+1)