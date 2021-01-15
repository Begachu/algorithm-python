# A+B - 8
import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    _input = input().split(' ')
    x = int(_input[0])
    y = int(_input[1])
    print("Case #%d: %d + %d = %d"%(i+1, x, y, x+y))