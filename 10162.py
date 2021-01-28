# 전자레인지
N = int(input())
if N%10!=0:
    print(-1)
else:
    print(N//300,(N%300)//60,(N%60)//10)