#ACM 호텔

N = int(input())

for i in range(N):
    _input = input().split(' ')
    H = int(_input[0])
    W = int(_input[1])
    X = int(_input[2])-1

    yy = X%H+1
    xx = X+1
    if yy==H:
        xx -= 1 
    xx = xx//H+1
    print(yy*100+xx)
