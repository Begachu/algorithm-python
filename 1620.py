# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

(N, M) = list(map(int, input().split()))
dic = dict()
for n in range(N):
    pokemon = input().strip()
    dic[pokemon] = n+1
    dic[str(n+1)] = pokemon
for m in range(M):
    print(dic[input().strip()])