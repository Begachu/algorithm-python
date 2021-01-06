_input = input().split(' ')

N = int(_input[0])
X = int(_input[1])

_input = input().split(' ')
result = []

for index in _input:
    if X>int(index):
        result.append(index)

print(' '.join(result))
