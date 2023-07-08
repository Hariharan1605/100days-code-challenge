T = int(input())
for i in range (0,T) :
    N,X = map(int,input().split())
    if X%N==0 :
        print("YES")
    else :
        print("NO")