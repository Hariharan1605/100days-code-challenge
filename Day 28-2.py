N = int(input())
flag=True
for i in range(0,N) :
    for j in range(0,i+1) :
        if flag==True :
            print(1,end=" ")
        else :
            print(0,end=" ")
        flag = bool(1-flag)
    if i%2 != 0 :
        flag = bool(1-flag)
    print(end="\n")