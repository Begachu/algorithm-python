# 파티가 끝나고 난 뒤
(L, P) = list(map(int, input().split()))
cnt = list(map(int, input().split()))
for i in range(5):
    cnt[i] -= L*P
print(' '.join(list(map(str, cnt))))