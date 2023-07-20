N = int(input())
for i in range(0,2*N-1) :
    if i<N :
        for j in range(0,i+1) :
            print("*",end=" ")
    else :
        for j in range(0,2*N-i-1) :
            print("*",end=" ")
    print(end="\n")