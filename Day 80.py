class Solution:
    def findTwoElement( self,arr, n):
        arr.sort()
        B = []
        i = n-1
        temp=0
        while i>=1 :
            if arr[i] == arr[i-1] :
                B.append(arr[i])
            if arr[i]-1 != arr[i-1] and arr[i] != arr[i-1] :
                num = arr[i] - 1
                temp=1
            i=i-1
        if temp == 0 :
            if arr[0] == 1 :
                num = arr[n-1]+1
            else :
                num = 1
        B.append(num)
        return B
if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends