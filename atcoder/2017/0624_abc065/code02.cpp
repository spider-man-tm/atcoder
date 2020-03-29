#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> vec(n);
    for (int i=0; i<n; i++) {
        cin >> vec.at(i);
    }
    int ans = 0;
    int tmp = 1;

    for (int i=0; i<n; i++) {
        ans++;
        tmp = vec.at(tmp-1);
        if (tmp==2) {
            cout << ans << endl;
            break;
            }
    }
    if (ans==n) cout << -1 << endl;
}