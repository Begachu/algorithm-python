# 게임을 만든 동준이
import sys
input = sys.stdin.readline

N = int(input())
save = [0]*N
result = 0
for i in range(N):
    save[i] = int(input())
for i in range(N-2, -1, -1):
    temp = save[i]-save[i+1]
    if temp>=0:
        result += temp+1
        save[i] -= temp+1
print(result)