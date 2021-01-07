# Hashing

N = int(input())
_input = input()

result = 0
_r = 1

for i in range(N):
    result += (ord(_input[i])-ord('a')+1)*_r
    _r *= 31

result %= 1234567891

print(result)