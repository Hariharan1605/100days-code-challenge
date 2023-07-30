bi = input("Enter Binary : ")
bi = bi[::-1]
j = 0
sum = 0
for i in bi :
    if i=='1' :
        sum = sum + 2**(j)
    j+=1
print(sum)