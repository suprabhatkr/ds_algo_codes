#include<bits/stdc++.h> 
using namespace std;
typedef long long int ll;
ll min(ll a, ll b){
	if(a>b){
		return b;
	}
	return a;
}
void show_dp(vector<vector<ll>> dp){
	for(int i=0;i<dp.size();i++){
		for(int j=0;j<dp.size();j++){
			cout<<dp[i][j]<<" ";
		}
		cout<<endl;
	}
}
void func(vector<ll> &A,vector<vector<ll>> &dp,int n,int j,int k){
	if (k<0 or j>n-1 or j>k){
		return;
	}
	if(dp[j][k]!=-1){
		return;
	}
	func(A,dp,n,j+1,k);
	func(A,dp,n,j,k-1);
	dp[j][k]=0;
	if(j<n-1 and k>0 and j<k){
		dp[j][k]=min(dp[j+1][k],dp[j][k-1]);
	}
	else if(j<n-1 and j<k){
		dp[j][k]=dp[j+1][k];
	}
	else if(k>0 and j<k){
		dp[j][k]=dp[j][k-1];
	}
	dp[j][k]+=(A[k]-A[j]);
	//cout<<j<<k<<endl;
	//show_dp(dp);
	return;
}
int main(){
	int n;
	cin>>n;
	vector<ll> A(n,0);
	vector<vector<ll>> dp(n,vector<ll>(n,-1));
	for(int i=0;i<n;i++){
		cin>>A[i];
	}
	sort(A.begin(),A.end());
	func(A,dp,n,0,n-1);
	cout<<dp[0][n-1]<<endl;
	return 0;
}