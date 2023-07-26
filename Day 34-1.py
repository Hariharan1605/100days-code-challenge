class Solution:
    def reverse(self, x: int) -> int:
        n = x
        if x<0:
            x=x*(-1)
        sum=0
        while x>0 :
            sum = sum*10 + x%10
            x = x//10
        if sum not in range(-2147483648,2147483647 ) :
            return 0
        if n<0 :
            return -1*sum
        else :
            return sum
x = int(input())
ob = Solution()
print(ob.reverse(x))