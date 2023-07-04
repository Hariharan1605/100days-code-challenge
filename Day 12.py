T = int(input())
for i in range(0,T) :
    A,B = map(int,input().split())
    if (A/10)>(B/20) :
        print("First")
    elif (A/10)<(B/20) :
        print("Second")
    else :
        print("Any")