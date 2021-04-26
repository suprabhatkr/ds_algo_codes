def func(curr,score,i,j,n,m):
	if i<0 or j<0 or i>=n or j>=m:
		return 
	if curr==kk[0]:
		mx[0]=min(score,mx[0])
		return 
	else:
		if j<m-1:
			func(curr+1,score+A[i][j],i,j+1,n,m)
		if j>0: 
			func(curr+1,score+A[i][j-1],i,j-1,n,m) 
		if i<n-1:
			func(curr+1,score+B[i][j],i+1,j,n,m) 
		if i>0:
			func(curr+1,score+B[i-1][j],i-1,j,n,m)

n,m,k=map(int,input().split())
A,B=[],[]
for i in range(n):
	A.append(list(map(int,input().split()))) 
for i in range(n-1):
	B.append(list(map(int,input().split()))) 
if k%2==0:
	kk=[k//2]
	for i in range(n):
		for j in range(m):
			mx=[10**9] 
			func(0,0,i,j,n,m) 
			print(mx[0]*2,end=' ')
		print('')
else:
	for i in range(n):
		for j in range(m):
			print(-1,end=' ')
		print('')

