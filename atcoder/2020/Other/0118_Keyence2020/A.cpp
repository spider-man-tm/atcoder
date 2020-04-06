#include <bits/stdc++.h>
using namespace std;

int main() {
    int h, w, n;
    cin >> h >> w >> n;
    int total = h*w;
    int kesu = max(h, w);

    if (n%kesu==0) {
        cout << n/kesu << endl;
    }
    else {
        cout << n/kesu + 1 << endl;
    }
}