#include<iostream>
#include <algorithm>

long long pre[100005];
long long suf[100005];
long long arr[100005];
long long res[100005];
using namespace std;

long long cal(long long zu[100005], int m, int n){
    long long res = 0;
    
    for (int i = m; i <= n; i++)
    {
        res = max(res, zu[i]);
    }
    return res;
}

int main()
{
    int N;
    cin >> N;
    int i = 1;
    for (int i = 1; i <= N; i++){
        cin >> arr[i];
    }
    pre[0] = pre[N + 1] = suf[0] = suf[N + 1] = 0;
    for (int i = 1; i<N; i++){
        pre[i] = pre[i - 1] ^ arr[i];
    }
    for (int i = N; i >= 1; i--){
        suf[i] = suf[i + 1] ^ arr[i];
    }
    long long ans = 0;
    for (int i = 1; i <= N; i++){
        ans = max(ans, max(cal(pre, 0, i), cal(suf, i + 1, N)));

    }
    cout << ans << endl;
    return 0;
}