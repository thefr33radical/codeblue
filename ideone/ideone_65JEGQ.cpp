/* Monkey Jumps */
#include <bits/stdc++.h>
using namespace std;

int getMedian(vector<int> &vec){
	int count1 = 0, count2;
	for(int i = 0; i < vec.size(); i++){
		if(vec[i] == 1){
			count1++;
		}
	}
	if(count1 == 0){
		return -1;
	}
	count1 = (count1 + 1) / 2;
	count2 = 0;
	for(int i = 0; i < vec.size(); i++){
		if(vec[i] == 1){
			count2++;
		}
		if(count1 == count2){
			return i;
		}
	}
	return -1;
}

int countJumps(vector<int> &vec){
	int median = getMedian(vec);
	int n = vec.size();
	if(median == -1){
		return 0;
	}
	int i = median - 1, flag = 0, empty, jumps = 0;
	empty = median;
	while(i >= 0){
		if(vec[i] == 1 && !flag){
			i--;
			continue;
		} else{
			if(vec[i] == 0 && vec[i+1] == 1){
				empty = i;
			} else if(vec[i] == 1){
				jumps += empty - i;
				vec[empty] = 1;
				empty--;
			}
		    flag = 1;
			i--;
		}
	}
	i = median + 1;
	empty = median;
	flag = 0;
	while(i < n){
		if(vec[i] == 1 && !flag){
			i++;
			continue;
		} else{
		    flag = 1;
			if(vec[i] == 0 && vec[i-1] == 1){
				empty = i;
			} else if(vec[i] == 1){
				jumps += i - empty;
				vec[empty] = 1;
				empty++;
            }
			i++;
		}
	}
	return jumps;
}

int main() {
	int arr[] = {1, 1, 1, 1, 1, 1, 0, 0, 1};
	int n = sizeof(arr) / sizeof(arr[0]);
	vector<int> vec(arr, arr+n);
	int minJumps = countJumps(vec);
	cout << minJumps << endl;	
	return 0;
}