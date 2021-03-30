# 좌표 압축
N = int(input())
X = list(map(int, input().split()))
dic = dict()

temp = sorted(list(set(X)))
for i in range(len(temp)):
    dic[temp[i]] = i

result = []
for x in X:
    result.append(str(dic[x]))
print(' '.join(result))