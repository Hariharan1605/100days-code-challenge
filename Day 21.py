T = int(input())
for i in range(0,T) :
    s = int(input())
    if s<1500 :
        print(s + 0.1*s + 0.9*s)
    else :
        print(s + 500 + 0.98*s)