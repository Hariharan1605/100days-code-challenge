class Solution:
def merge(self, l1: List[int], m: int, l2: List[int], n: int) -> None:
    for i in range (0,m) :
        l2.append(l1[i])
    l2.sort()
    j=0
    for i in l2 :
        l1[j] = i
        j+=1
