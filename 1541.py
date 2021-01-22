# 잃어버린 괄호
S = input()
result = 0
start = 0
minus = False
for i in range(1, len(S)):
    if S[i]=="+" or S[i]=="-":
        temp = int(S[start:i])
        start = i
        if temp<0:
            minus = True
        else:
            if minus:
                temp = -temp
        result += temp
temp = int(S[start:])
if temp>0:
    if minus:
        temp = -temp
result += temp
print(result)