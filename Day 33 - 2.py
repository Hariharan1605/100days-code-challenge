class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 :
            return False
        else :
            sum=0
            num = x
            while x>0 :
                sum = sum*10 + x%10
                x = x//10
            if sum==num :
                return True
            else :
                return False
x = int(input())
ob = Solution()
print(ob.isPalindrome(x))
