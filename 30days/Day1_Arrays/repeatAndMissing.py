#Find Repeat and Missing Number
class Solution():
    def findTwoElement(self,arr,n):
        xr1,xr2,xr3=0,0,0
        sm,actsm=0,(n*(n+1))//2
        for i in range(n):
            sm+=arr[i]
            xr1=xr1^(i+1)^arr[i];
        small=1
        while xr1&1==0:
            small*=2 
            xr1=xr1>>1
        for i in range(n):
            if small&(i+1):
                xr2=xr2^(i+1) 
            else:
                xr3=xr3^(i+1) 
            if small&arr[i]:
                xr2=xr2^arr[i]
            else:
                xr3=xr3^arr[i] 
        if sm>actsm:
            if xr3>xr2:
                return (xr3,xr2) 
            else:
                return (xr2,xr3) 
        else:
            if xr3>xr2:
                return (xr2,xr3)
            else:
                return (xr3,xr2) 

