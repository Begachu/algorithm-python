# 홀수
_min = 100
odd = 0
for i in range(7):
    index = int(input())
    if index%2==1:
        odd += index
        if _min>index:
            _min = index
if odd==0:
    print(-1)
else:
    print(odd)
    print(_min)