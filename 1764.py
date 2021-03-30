# 듣보잡
import sys
input = sys.stdin.readline

dic = dict()
result = []
(N, M) = list(map(int, input().split()))
for n in range(N):
    word = input().strip()
    dic[word] = True
for m in range(M):
    word = input().strip()
    if word in dic:
        del dic[word]
        result.append(word)
result.sort()
print(len(result))
for word in result:
    print(word)