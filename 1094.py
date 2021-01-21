# 막대기
X = int(input())
_len = 64
result = 0
while X>0:
    if X>=_len:
        X -= _len
        result += 1
    _len = _len//2
print(result)