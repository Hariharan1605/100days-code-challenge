T = int(input())
for i in range(0,T) :
    lis = list(map(int,input().split()))
    Max = max(lis)
    s_max=0
    for i in range(0,3) :
        if lis[i]!=Max :
            if s_max<lis[i] :
                s_max = lis[i]
    print(s_max)
