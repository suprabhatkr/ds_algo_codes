#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
class Solution:
    def sort012(self,arr,n):
        c0,c1=0,0 
        for a in arr:
            if a==0:
                c0+=1
            elif a==1:
                c1+=1 
        i=0 
        while c0>0:
            arr[i]=0 
            i+=1 
            c0-=1 
        while c1>0:
            arr[i]=1 
            i+=1 
            c1-=1 
        while i<n:
            arr[i]=2
            i+=1

S=Solution()
n=int(input())
arr=list(map(int,input().split())) 
S.sort012(arr,n) 
for a in arr:
    print(a,end=' ') 

