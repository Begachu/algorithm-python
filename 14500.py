# 테트로미노
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [list(map(int, input().split())) for n in range(N)]
result = 0

# type 1
for m in range(M-4):
    for n in range(N):
        temp = sum(S[n][m:m+4])
        if temp>result:
            result = temp

# type 1 - R
for n in range(N-4):
    for m in range(M):
        temp = sum([S[i][m] for i in range(n, n+4)])
        print(temp)
        if temp>result:
            result = temp

# type 2
for n in range(N-2):
    for m in range(M-2):
        temp = sum([sum(S[i][n:n+2]) for i in range(m, m+2)])
        if result<temp:
            result = temp

# type 3
for n in range(N-2):
    for m in range(M-3):
        temp = sum([S[i][n] for i in range(m, m+3)])
        temp += S[m+2][n+1]
        if result<temp:
            result = temp

# type 3 - M
for n in range(N-2):
    for m in range(M-3):
        temp = sum([S[i][n+1] for i in range(m, m+3)])
        temp += S[m+2][n]
        if result<temp:
            result = temp

# type 3 - R
for n in range(N-3):
    for m in range(M-2):
        temp = sum(S[m][n:n+3])
        temp += S[m+1][n+2]
        if result<temp:
            result = temp

# type 3 - RM
for n in range(N-3):
    for m in range(M-2):
        temp = sum(S[m][n:n+3])
        temp += S[m+1][n]
        if result<temp:
            result = temp

# type 3 - RR
for n in range(N-2):
    for m in range(M-3):
        temp = sum([S[i][n+1] for i in range(m, m+3)])
        temp += S[m][n]
        if result<temp:
            result = temp

# type 3 - RRM
for n in range(N-2):
    for m in range(M-3):
        temp = sum([S[i][n] for i in range(m, m+3)])
        temp += S[m][n+1]
        if result<temp:
            result = temp

# type 3 - RRR
for n in range(N-3):
    for m in range(M-2):
        temp = sum(S[m+1][n:n+3])
        temp += S[m][n+2]
        if result<temp:
            result = temp

# type 3 - RRRM
for n in range(N-3):
    for m in range(M-2):
        temp = sum(S[m+1][n:n+3])
        temp += S[m][n]
        if result<temp:
            result = temp

print(result)