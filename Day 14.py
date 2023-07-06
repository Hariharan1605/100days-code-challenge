T = int(input())
for i in range(0,T) :
    X,A,B = map(int,input().split())
    if X<= A*1 + B*2 :
        print("QUALIFY")
    else :
        print("NOTQUALIFY")