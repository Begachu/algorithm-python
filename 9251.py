# LCS (9251)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

s1 = input().strip()
s2 = input().strip()

cnt = [[-1 for i in range(1000)] for j in range(1000)]

def dp(c1, c2):
	if c1==len(s1) or c2==len(s2):
		return 0
	if cnt[c1][c2]!=-1:
		return cnt[c1][c2]
	have = False
	_c2 = 0
	for i in range(c2, len(s2)):
		if s1[c1]==s2[i]:
			_c2 = i+1
			have = True
			break
	if have:
		cnt[c1][c2] = max(1+dp(c1+1, _c2), dp(c1+1, c2))
	else:
		cnt[c1][c2] = dp(c1+1, c2)
	return cnt[c1][c2]

print(dp(0, 0))
