#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void genx(vector<int> &num,int length)
{	int flag=1;

	// segment to check whether all are 9*******************************
	for(int i=0;i<num.size();i++)
		{	if(num[i]!=9)
			{	
				flag=0;
			break;	
			}
		}
	if(flag==1)  
		{		cout<<1;
				for(int i=0;i<num.size()-1;i++)
					cout<<0;

				cout<<1;
			return;
		}
	// segment to check whether all are 9 *******************************

	int mid=num.size()/2;
	bool leftsmall=false;
	
	int i=mid-1;
	int j=(num.size()%2)?mid+1:mid;

	while(i>=0&&num[i]==num[j])
	{	i--;
		j++;
		}

	 if ( i < 0 || num[i] < num[j])
				leftsmall=true;
	while(i>=0)
	{	num[j]=num[i];
		i--;
		j++;
	}
	
	
	 if (leftsmall == true)
    {
        int carry = 1;
        i = mid - 1;
 
        // If there are odd digits, then increment
        // the middle digit and store the carry
        if (num.size()%2 == 1)
        {
            num[mid] += carry;
            carry = num[mid] / 10;
            num[mid] %= 10;
            j = mid + 1;
        }
        else
            j = mid;
 
        // Add 1 to the rightmost digit of the left side, propagate the carry 
        // towards MSB digit and simultaneously copying mirror of the left side 
        // to the right side.
        while (i >= 0)
        {
            num[i] += carry;
            carry = num[i] / 10;
            num[i] %= 10;
            num[j++] = num[i--]; // copy mirror to right
        }
    }


	for(int i=0;i<num.size();i++)
		cout<<num[i];
}

int main() {
	string n="941878322";
			string y;	
	vector<int> num;
	vector<int> num2;

	for(int i=0;i<n.length();i++)
	{	num.insert(num.begin()+i,n[i]-'0');
	}

for(auto it=num.begin();it!=num.end();it++)
		{	num2.push_back(*it);
		cout<<*it;
		}
	cout<<"\n";
 genx( num2, num2.size() );
 
    return 0;
}