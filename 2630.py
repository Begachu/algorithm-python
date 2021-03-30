# 색종이 만들기
import sys
input = sys.stdin.readline

N = int(input())
paper = [list(input().strip().split()) for i in range(N)]

def dc(n, x, y):
    if n==1:
        if paper[x][y]=='1':
            return (1, 0)
        else:
            return (0, 1)
    else:
        _all_blue = True
        _all_white = True
        (blue, white) = dc(n//2, x, y)
        if blue!=1:
            _all_blue = False
        if white!=1:
            _all_white = False

        temp = dc(n//2, x+n//2, y+n//2)
        blue += temp[0]
        white += temp[1]
        if temp[0]!=1:
            _all_blue = False
        if temp[1]!=1:
            _all_white = False

        temp = dc(n//2, x, y+n//2)
        blue += temp[0]
        white += temp[1]
        if temp[0]!=1:
            _all_blue = False
        if temp[1]!=1:
            _all_white = False

        temp = dc(n//2, x+n//2, y)
        blue += temp[0]
        white += temp[1]
        if temp[0]!=1:
            _all_blue = False
        if temp[1]!=1:
            _all_white = False

        if _all_blue:
            blue = 1
        if _all_white:
            white = 1
        return (blue, white)

(B, W) = dc(N, 0, 0)
print(W)
print(B)