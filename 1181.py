# 단어 정렬

N = int(input())
_array = []

for i in range(N):
    _array.append(input())

_array = list(set(_array))
_array.sort()
_array.sort(key=len)

print('\n'.join(_array))