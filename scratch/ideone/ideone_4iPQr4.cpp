#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int n;
    cin >> n;
    string x="010";
    string B;
    cin >> B;
    int count=0;
     size_t found=B.find(x);
    
    while(found!=string::npos)
    {       B.replace(found,x.length(),"");
            found=B.find(x);
        count++;
    }
    cout<<count;
    return 0;
}
