# 최대공약수와 최소공배수

def greatest_common_factor(a, b):
    while a>0:
        temp = b
        b = a
        a = temp%a

    return b

def least_common_multiple(a, b):
    temp_a = a
    temp_b = b
    while temp_a!=temp_b:
        if temp_a<temp_b:
            temp_a += a
        else:
            temp_b += b

    return temp_b

if __name__=="__main__":
    _input = input().split(" ")

    if int(_input[0])>int(_input[1]):
        A = int(_input[1])
        B = int(_input[0])
    else:
        A = int(_input[0])
        B = int(_input[1])

    print(greatest_common_factor(A,B))
    print(least_common_multiple(A, B))