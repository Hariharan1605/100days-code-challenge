n = int(input("Enter a decimal no : "))
str1 = ""
while n>0 :
    str1 = str1 + str(n%2)
    n//=2
print(str1[::-1])
