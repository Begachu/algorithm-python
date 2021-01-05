_input = int(input())

for i in range(2):
    _input *= int(input())

_input = str(_input)

for i in range(10):
    print(_input.count(str(i)))