#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, ans;
    cin >> n;

    for (int i=1; i<n+1; i++) {
        ans += i;
    }
    cout << ans << endl;
}