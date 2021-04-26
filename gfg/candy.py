#https://www.geeksforgeeks.org/count-ways-to-select-n-pairs-of-candies-of-distinct-colors-dynamic-programming-bitmasking/
def no_of_ways(tab,n,mp={},i=0):
    if count==n:
        return 1
    count=0
    for j in range(n):
        if j not in mp and mp[j]==0 and tab[i][j]==1:
            if dp[i][j]!=-1:
                count+=dp[i][j]
            else:
                mp[j]=1
                count+=no_of_ways(tab,n,mp,i+1)
                mp[j]=0
    return count 
dp=[] 
for i in range(n):
    dp.append([])
    for j in range(n):
        dp[i].append(-1) 
print(no_of_ways(arr,n))

