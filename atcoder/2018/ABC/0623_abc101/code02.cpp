#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, n_origin, s, keta;
    cin >> n;
    n_origin = n;
    s = 0;
    keta = 10;

    while (n >= 1) {
        s += n%10;
        n /= keta;
    }

    if (n_origin%s == 0) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
}