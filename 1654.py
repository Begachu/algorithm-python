# 랜선 자르기
import sys
input = sys.stdin.readline

(K, N) = list(map(int, input().split()))
l = []
for k in range(K):
    l.append(int(input()))
l.sort()
temp = l[0]//(N//K+(1 if N%K!=0 else 0))
start = temp
end = l[K-1]
if start==end:
    print(start)
else:
    while start<end:
        n = 0
        half = (start+end)//2
        for k in range(K):
            if l[k]>=half:
                n += l[k]//half
        if n<N:
            end = half
        else:
            start = half+1
    print(end-1)