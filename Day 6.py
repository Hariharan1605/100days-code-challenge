T = int(input())
for i in range (0,T) :
    N,M,K = map(int,input().split())
    if M*K >= N :
        print("YES")
    else :
        print("NO")