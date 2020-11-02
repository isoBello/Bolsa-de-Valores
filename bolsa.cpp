#include <iostream>
#include <bits/stdc++.h>
#include<string>

using namespace std;
typedef long long ll;

const int N = 200000;
ll dp[N][2];
ll dias[N];
int n, C;

ll bolsa(){
    dp[n][0] = dp[n][1] = false;
    for(int i = n - 1; i >= 0; ++i){
        for(int j = 0; j <= 1; ++j){
            ll x = (dp[i][j] ? dias[i] : -(dias[i] + C));
            dp[i][j] = max(x + dp[i + 1][!j], dp[i + 1][j]);
        }
    }
    return dp[0][0];
}

int main() {
 
    cin>>n>>C;

    for (int i = 0; i < n; ++i)
        cin >> dias[i];

    memset(dp, -1, sizeof dp);

    int ans = bolsa();
    cout << ans << endl;
    return 0;
}