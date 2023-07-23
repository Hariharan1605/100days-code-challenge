

class Solution:
    def printTriangle(self, N):
        flag=-2
        for i in range(0,N) :
            flag=flag+2
            for j in range(0,2*N) :
                if j<N-i or j>=N-i+flag :
                    print("*",end="")
                else :
                    print(end=" ")
            print(end="\n")
        flag=flag+2
        for i in range(0,N) :
            flag=flag-2
            for j in range(0,2*N) :
                if j<=i or j>i+flag :
                    print("*",end="")
                else :
                    print(end=" ")
            print(end="\n")   



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
