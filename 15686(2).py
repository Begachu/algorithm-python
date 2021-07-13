# 치킨 배달
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
C = [list(map(int, input().split())) for n in range(N)] # city
H = []  # house
S = []  # store

for i in range(N):
    for j in range(N):
        if C[i][j]==1:
            H.append((i, j))
        elif C[i][j]==2:
            S.append((i, j))

D = [[abs(s[0]-h[0])+abs(s[1]-h[1]) for s in S] for h in H]

selected = [0 for i in S]
save = [N*N for i in H]

while sum(selected)<M:
    best = [N*N for i in range(len(H))]
    pick = -1
    for s in range(len(S)):
        if selected[s]==1:
            continue
        temp = [min(save[i], D[i][s]) for i in range(len(H))]
        if sum(best)>sum(temp):
            best = temp
            pick = s
    selected[pick] = 1
    save = best

print(sum(save))
