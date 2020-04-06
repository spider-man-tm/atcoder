#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k, q;
    cin >> n >> k >> q;
    vector<int> a(q);

    for (int i=0; i<q; i++) {
        cin >> a.at(i);
    }

    vector<int> nn(n), kk(n, k), qq(n, q);

    for (int i=0; i<q; i++) {
        int idx = a.at(i) - 1;
        nn.at(idx) ++;
    }

    for (int i=0; i<n; i++) {
        int ans = kk.at(i) - qq.at(i) + nn.at(i);
        if (ans > 0) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
}