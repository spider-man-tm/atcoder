#include <bits/stdc++.h>
using namespace std;

int main() {
    long long x, y, z;
    cin >> x >> y >> z;
    long long mod = x%(y+z);
    long long ans = x/(y+z);
    if (mod<z) ans--;

    cout << ans << endl;
}