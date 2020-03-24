#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, k, x, y, ans;
    cin >> n >> k >> x >> y;
    for (long long i=1; i<n+1; i++) {
        if (i<=k) ans += x;
        else ans += y;
    }
    cout << ans << endl;
}