#include <iostream>
using namespace std;

int main() {
	//code

	int i,j,maxlen,n;

	cin>>n;

	int arr[n];
	int res[n];



	for(i=0;i<n;i++)
	{
	cin>>arr[i];
	}


	for(i=0;i<n;i++)
	{
	res[i]=1;
	}

	i=0;
	j=0;
	while(i<n)
	{
        while(j<i)
            {
                if(arr[j]<arr[i])
                    res[i]=res[i]+1;

                j++;
            }

        j=0;
        i++;

    }

    maxlen=res[0];
	for(i=0;i<n;i++)
	{
        if(res[i]>maxlen)
            maxlen=res[i];



	}
cout<<"\n--"<<sizeof(arr)/sizeof(int);
cout<<maxlen;
	return 0;
}
