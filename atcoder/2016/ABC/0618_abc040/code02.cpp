#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, w, h, mod;
    cin >> n;
    int minn = pow(10, 9);

    for (int i=1; i<n+1; i++) {
        w = i;
        h = (n/w);
        mod = n - (w*h);
        int ans = max(w, h) - min(w, h) + mod;

        if (ans < minn) {
            minn = ans;
        }
    }
    cout << minn << endl;
}