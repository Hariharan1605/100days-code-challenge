N = int(input())
for i in range(0,N) :
    for j in range(0,2*N-1) :
        if j<N-i-1 :
            print(" ",end="")
        elif j<N+i :
            print("*",end="")
    print(end="\n")