# 비밀번호 찾기
import sys
input = sys.stdin.readline

(N, M) = list(map(int, input().split()))
dic = dict()
for n in range(N):
    (site, pw) = list(input().strip().split())
    dic[site] = pw
for m in range(M):
    site = input().strip()
    print(dic[site])