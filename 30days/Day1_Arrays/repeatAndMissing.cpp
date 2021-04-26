// Find Repeat and Missing 
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

class Solution{
	public:
		int *findTwoElement(int *arr,int n){
			static int ans[2]={-1,-1};
			int sqr=0,sm=0,actSm=((n*(n+1))/2),actsqr=((n*(n+1)*(2*n+1))/6);
			for(int i=0;i<n;i++){
				sm+=arr[i];
				sqr+=arr[i]*arr[i];
			}
			int dif,sqdif;
			if (actSm>sm){
				dif=actSm-sm;
				sqdif=(actsqr-sqr);
				ans[1]=(dif+(sqdif/dif))/2;
				ans[0]=ans[1]-dif;
			}
			else{
				dif=sm-actSm;
				sqdif=sqr-actsqr;
				ans[0]=(dif+(sqdif/dif))/2;
				ans[1]=ans[0]-dif;
			}
			return ans;
		}
};
int main(){
	int n;
	cin>>n;
	int arr[n];
	for (int i=0;i<n;i++){
		cin>>arr[i];
	}
	Solution S;
	int *ans=S.findTwoElement(arr,n);
	cout<<ans[0]<<" "<<ans[1]<<endl;
}
