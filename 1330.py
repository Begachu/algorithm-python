_input = input().split(' ')

x = int(_input[0])
y = int(_input[1])


if x>y:
    print(">")
elif x<y:
    print("<")
else:
    print("==")