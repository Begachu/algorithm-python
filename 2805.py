# 나무 자르기
import sys
input = sys.stdin.readline

hight = 0
n = 0

# get input data
(N, M) = list(map(int, input().split(' ')))
trees = list(map(int, input().split(' ')))
cache = [0 for i in range(N)]


# compute
trees.sort()
for i in range(N-2, -1, -1):
    cache[i] = (trees[i+1]-trees[i])*(N-i-1)+cache[i+1]
    if cache[i]>=M:
        hight = trees[i]
        n = i
        break


if hight==0:
    temp = cache[0]
    start = 0
    end = trees[0]

    while start<end:
        half = (start+end)//2
        if half*N+temp==M:
            start = half
            break
        elif half*N+temp>M:
            end = half
        else:
            start = half+1
    print(trees[0]-start)

elif cache[n]==M:
    print(hight)

elif cache[n]>M:
    temp = cache[n]
    start = 0
    end = trees[n+1]-hight

    while start<end:
        half = (start+end)//2
        if temp-half*(N-1-n)==M:
            start = half+1
            break
        elif temp-half*(N-1-n)<M:
            end = half
        else:
            start = half+1
    print(hight+start-1)
