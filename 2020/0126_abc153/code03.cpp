#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    long long ans;
    cin >> n >> k;
    
    vector<int> vec(n);
    for (int i=0; i < n; i++) {
        cin >> vec.at(i);
    }
    sort(vec.begin(), vec.end());
    reverse(vec.begin(), vec.end());

    if (k>=n) {
        cout << 0 << endl;
    } else {
        for (int i=0; i<n; i++) {
            if (i>=k) {
                ans += vec[i];
            }
        }
        cout << ans << endl;
    }
}