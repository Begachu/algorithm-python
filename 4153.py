while True:
    _input = input().split(' ')
    if _input[0]=='0' and _input[1]=='0' and _input[2]=='0':
        break
    else:
        _temp = [int(_input[0]), int(_input[1]), int(_input[2])]
        _temp.sort()
        
        if _temp[0]*_temp[0]+_temp[1]*_temp[1] == _temp[2]*_temp[2]:
            print("right")
        else:
            print("wrong")