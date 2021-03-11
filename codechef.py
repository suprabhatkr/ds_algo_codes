N=int(input()) 
A=[] 
for n in range(N):
	A.append(list(map(int,input().split()))) 
L=[]
mp={}
pos=1
for i in range(N):
	L.append(A[i][i])
	mp[A[i][i]]=pos 
	pos+=1
parent={}
for i in range(N):
	mn=10**9
	for j in range(N):
		if i!=j and A[i][j]<mn:
			mn=A[i][j]
	if mn not in mp:
		mp[mn]=pos 
		pos+=1 
	parent[i]=mp[mn]

