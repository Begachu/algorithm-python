_input = input().split(' ')

x = int(_input[0])
y = int(_input[1])
w = int(_input[2])
h = int(_input[3])

score = [x, y, w-x, h-y]
score.sort()
print(score[0])