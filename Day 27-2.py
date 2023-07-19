N = int(input())
left=0
right=2*N-1
for i in range(0,N) :
    for j in range(0,2*N-1) :
        if j<left :
            print(" ",end="")
        elif j<right :
            print("*",end="")
    left=left+1
    right=right-1
    print(end="\n")