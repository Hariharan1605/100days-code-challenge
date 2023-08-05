class Solution:
    def mergesort(self,arr,l,r) :
        if l>=r :
            return
        mid = (l+r)//2
        ob = Solution()
        ob = Solution()
        ob.mergesort(arr,l,mid)
        ob.mergesort(arr,mid+1,r)

        left = l
        right = mid+1
        n1 = mid-l+1
        n2 = r-mid
        lefthalf = []
        righthalf = []
        for i in range(n1) :
            lefthalf.append(arr[left+i])
        for j in range(n2) :
            righthalf.append(arr[right+j])
        index = l
        p1=0
        p2=0
        while p1<n1 and p2<n2 :
            if lefthalf[p1] <= righthalf[p2] :
                arr[index] = lefthalf[p1]
                index+=1
                p1+=1
            else :
                arr[index] = righthalf[p2]
                p2+=1
                index+=1
        while p1 < n1 :
            arr[index] = lefthalf[p1]
            index+=1
            p1+=1
        while p2 < n2 :
            arr[index] = righthalf[p2]
            index += 1
            p2 += 1




#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergesort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends