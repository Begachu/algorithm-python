# 날짜 계산
(E, S, M) = list(map(int, input().split(' ')))
E -= 1
S -= 1
M -= 1
mult = 15*28*19
(n1, n2, n3) = (28*19, 15*19, 15*28)
(s1, s2, s3) = (1, 1, 1)
while (s1*n1)%15!=E:
    s1 += 1
while (s2*n2)%28!=S:
    s2 += 1
while (s3*n3)%19!=M:
    s3 += 1

result = n1*s1+n2*s2+n3*s3
print(result%mult+1)