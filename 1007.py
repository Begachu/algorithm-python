# 벡터 매칭
import sys
import math
input = sys.stdin.readline

def dp(p):
    if len(p)==2:
        w = round(math.sprt((p[0][0]-p[1][0])**2+(p[0][1]-p[1][1])**2), 6)
        a = math.atan(p[0][1]-p[1][1]/(p[0][0]-p[1][0]))
        return [(w, a)]
    else:
        

T = int(input())
for _ in range(T):
    N = int(input())
    p = []
    for n in range(N):
        p.append(list(map(int, input.split())))
    
    