#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> h(n);
    for (int i=0; i<n; i++) {
        cin >> h.at(i);
    }

    int cnt = 0;
    int before = 0;

    for (int i=0; i<n; i++) {
        if (before < h.at(i)) {
            cnt += h.at(i) - before;
        }
        before = h.at(i);
    }
    cout << cnt << endl;
}