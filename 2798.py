def blackjack():
    # first input line ( N : card amount, M : target number )
    _input = input().split(" ")
    N = int(_input[0])
    M = int(_input[1])
    
    # second input line ( card index )
    _input = input().split(" ")

    result = 0

    for i in range(N-2):
        temp1 = int(_input[i])
        for j in range(i+1, N-1):
            temp2 = temp1 + int(_input[j])
            for k in range(j+1, N):
                temp3 = temp2 + int(_input[k])

                # print("test: ", temp3)
                if temp3 > M :
                    continue
                elif temp3 == M:
                    return temp3
                else:
                    if M-temp3 < M-result :
                        result = temp3
    return result


if __name__ == "__main__":
    print(blackjack())