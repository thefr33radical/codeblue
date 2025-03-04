#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main() {
	// your code goes here
	
 long n,root_five,fibo;
 cin>>n;
 n=n+1;
 if(n==0||n==1)
 {	cout<<1;
 	return 0;
 }
 root_five=sqrt(5);
 fibo=(pow((1+root_five),n)-pow((1-root_five),n))/(pow(2,n)*root_five);
 cout<<fibo;
 	return 0;
}