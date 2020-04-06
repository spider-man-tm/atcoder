#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    long long mod = pow(10, 9)+7;
    cin >> n;
    long long ans = 1;
    for (long long i=1; i<n+1; i++) {
        ans *= i;
        ans %= mod;
    }
    cout << ans << endl;
}