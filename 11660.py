# 구간 합 구하기 5 (11660)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = [list(map(int, input().split())) for i in range(N)]
cnt = num
for y in range(N):
	for x in range(N):
		if x>0 and y>0:
			cnt[y][x] += cnt[y][x-1] + cnt[y-1][x] - cnt[y-1][x-1]
		elif x>0:
			cnt[y][x] += cnt[y][x-1]
		elif y>0:
			cnt[y][x] += cnt[y-1][x]


for i in range(M):
	x1, y1, x2, y2 = map(int, input().split())
	x1 -= 2
	y1 -= 2
	x2 -= 1
	y2 -= 1
	result = cnt[x2][y2]

	if x1>=0 and y1>=0:
		result += cnt[x1][y1]-cnt[x2][y1]-cnt[x1][y2]
	elif y1>=0:
		result -= cnt[x2][y1]
	elif x1>=0:
		result -= cnt[x1][y2]
	print(result)
	
