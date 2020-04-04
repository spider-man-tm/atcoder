#include <bits/stdc++.h>
using namespace std;

int main() {
    long long x, y, k;
    cin >> x >> y >> k;
    if (k<=y) {
        cout << x + k << endl;
    } else {
        cout << y + (x - (k-y)) << endl;
    }
}