dic = []

for i in range(26):
    dic.append([0, chr(i+65)])

_input = input()

for a in _input:
    a = ord(a)
    if a>=97:
        a -= 32
    
    dic[a-65][0] += 1

dic.sort(key=lambda a:a[0], reverse=True)
if dic[0][0] == dic[1][0]:
    print("?")
else:
    print(dic[0][1])