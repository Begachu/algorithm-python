dic = {}

for i in range(10):
    _index = int(input())
    mod = _index%42
    if mod in dic:
        dic[mod] += 1
    else:
        dic[mod] = 1

print(len(dic))