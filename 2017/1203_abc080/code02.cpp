#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, an, total;
    cin >> n;
    an = n;
    for (int i=0; i<n; i++) {
        total += an%10;  // 1の位, 10の位, ...
        an /= 10;
    }
    if (n%total==0) cout << "Yes" << endl;
    else cout << "No" << endl;
}