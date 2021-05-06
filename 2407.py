# 조합 (2407)
cnt = [i for i in range(1, 101)]
for i in range(1, 100):
	cnt[i] *= cnt[i-1]

n, m = map(int, input().split())
if n==m:
	print(1)
else:
	print(cnt[n-1]//(cnt[n-m-1]*cnt[m-1]))
