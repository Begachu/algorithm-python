# 쉽게 푸는 문제 (1292)
A, B = map(int, input().split())
cnt = [45]*1001
cnt[0] = 0
a = 1
num = 1
while num<45:
	for i in range(num):
		cnt[i+a] = num
	a += num
	num += 1

print(sum(cnt[A:B+1]))
