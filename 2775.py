# 부녀회장이 될테야

apartment = []

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())-1

    if k>=len(apartment):
        for h in range(k-len(apartment), k+1):
            apartment.append([])

    if n>len(apartment[k-1]):
        for h in range(k):
            old_len = len(apartment[h])
            for w in range(old_len, n+1):
                if w==0:
                    apartment[h].append(1)
                else:
                    pred = apartment[h][w-1]
                    under = w+1
                    if h>0:
                        under = apartment[h-1][w]
                    apartment[h].append(pred+under)
    print(apartment[k-1][n])