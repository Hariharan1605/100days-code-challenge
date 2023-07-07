T = int(input())
for i in range(0,T) :
    N = int(input())
    if N%4 == 0 :
        print(N//4)
    else :
        print(N//4 + 1)