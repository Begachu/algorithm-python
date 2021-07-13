# 돌 게임 (9655)
N = int(input())
cnt = [-1]*(N+1)

def dp(n, who):
	if cnt[n]==-1:
		if n==1 or n==3:
			cnt[n] = who
		else:
			if dp(n-1, (who+1)%2)==who:
				cnt[n] = who
			elif dp(n-3, (who+1)%2)==who:
				cnt[n] = who
			else:
				cnt[n] = (who+1)%2
	return cnt[n]

if dp(N, 0)==0:
	print("SK")
else:
	print("CY")
