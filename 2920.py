_input = input().split(' ')

temp = 0

if _input[0]=='1':
    temp = 1
    for i in _input:
        if int(i)!=temp:
            break
        else:
            temp += 1
    if temp==9:
        print("ascending")
    else:
        print("mixed")

elif _input[0]=='8':
    temp = 8
    for i in _input:
        if int(i)!=temp:
            break
        else:
            temp -= 1
    if temp==0:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")