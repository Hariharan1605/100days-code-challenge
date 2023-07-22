N = int(input())
for i in range(0,N) :
    for j in range(0,i+1) :
        print(chr(65+j),end="")
    print(end="\n");