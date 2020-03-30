#include <bits/stdc++.h>
using namespace std;

int main () {
    int n, ans;
    cin >> n;
    for (int i=0; i<n; i++) {
        int l, r;
        cin >> l >> r;
        ans += (r-l+1);
    }
    cout << ans;
}