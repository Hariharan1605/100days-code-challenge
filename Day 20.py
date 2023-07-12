T = int(input())
for i in range(0,T) :
    X = int(input())
    count = X//10
    if X%10 == 0 :
        print(count)
    elif X%10 == 5 :
        print(count+1)
    else :
        print(-1)