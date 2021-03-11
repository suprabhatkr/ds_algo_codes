T=int(input())
for t in range(T):
    n,u,r,d,l=(map(int,input().split()))
    max_r,max_l,max_u,max_d,min_r,min_l,min_u,min_d=n,n,n,n,0,0,0,0
    flag=True
    if u==0 and d==0 and (r>n-2 or l>n-2):
        flag=False
    elif l==0 and r==0 and (u>n-2 or d>n-2):
        flag=False
    elif l==0 and r==1 and ((u>n-2 and d>n-2)):
        flag=False
    elif l==1 and r==0 and ((u>n-2 and d>n-2)):
        flag=False
    elif u==0 and d==1 and ((l>n-2 and r>n-2)):
        flag=False
    elif u==1 and d==0 and ((l>n-2 and r>n-2)):
        flag=False
    elif u==0 and (l>n-1 or r>n-1):
        flag=False
    elif d==0 and (l>n-1 or r>n-1):
        flag=False
    elif l==0 and (u>n-1 or d>n-1):
        flag=False
    elif r==0 and (u>n-1 or d>n-1):
        flag=False
    elif r==1 and (u>n-1 and d>n-1):
        flag=False
    elif l==1 and (u>n-1 and d>n-1):
        flag=False
    elif d==1 and (r>n-1 and l>n-1):
        flag=False
    elif u==1 and (r>n-1 and l>n-1):
        flag=False
    if flag:
        print("yes") 
    else:
        print("no") 
