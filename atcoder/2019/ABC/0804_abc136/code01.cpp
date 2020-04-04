#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int ans = c - a + b;
    if (ans > 0) cout << ans << endl;
    else cout << 0 << endl;
}