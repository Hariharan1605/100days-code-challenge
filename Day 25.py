class Solution:
    def printSquare(self, N):
        for i in range(0,N) :
            for j in range(0,N) :
                print("* ",end="")
            print(end="\n")
N = int(input())
ob = Solution()
ob.printSquare(N)