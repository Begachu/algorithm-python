_input = input().split(" ")
n = int(_input[0])
m = int(_input[1])

_list = []
_input = input().split(" ")
for index in _input:
    _list.append(int(index))

_list = sorted(_list)

for i in range(m):
    _temp = _list[0] + _list[1]
    _list[0] = _temp
    _list[1] = _temp
    _list = sorted(_list)

print(sum(_list))


