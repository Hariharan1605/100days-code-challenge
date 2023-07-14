T = int(input())
for i in range(0,T) :
    N = int(input())
    l = list(map(int,input().split()))
    count=-1
    flag=0
    for i in range(N-1,-1,-1) :
        if l[i]>0 or l[i]<0 or flag==1 :
            count=count+1
            flag=1
    if N==1 :
            print(0)
    else :
        print(count)