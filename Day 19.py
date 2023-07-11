T = int(input())
for i in range(0,T) :
    N,M = map(int,input().split())
    if M>=N :
        print(N)
    else :
        print((N-M)*2 + M)