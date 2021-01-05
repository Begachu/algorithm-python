_input = input()[::-1].split(" ")

if int(_input[0])>int(_input[1]):
    print(_input[0])
else:
    print(_input[1])