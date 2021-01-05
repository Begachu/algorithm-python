result_1 = -1
result_2 = -1

for i in range(9):
    _input = int(input())
    
    if _input > result_1:
        result_1 = _input
        result_2 = i

print(result_1)
print(result_2+1)