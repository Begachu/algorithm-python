# 스티커 (9465)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100002)
cnt = None
sticker = None
N = None

def dp(x, y):
	global cnt
	if cnt[y][x]!=-1:
		return cnt[y][x]
	if x==N-1:
		cnt[y][x] = sticker[y][x]
		return cnt[y][x]
	temp = sticker[y][x] + dp(x+1, (y+1)%2)
	temp = max(temp, dp(x+1, y))
	cnt[y][x] = temp
	return cnt[y][x]

T = int(input())

for _ in range(T):
	N = int(input())
	cnt = [[-1 for i in range(N)] for j in range(2)]
	sticker = [list(map(int, input().split())) for j in range(2)]
	print(max(dp(0, 0), dp(0, 1)))
