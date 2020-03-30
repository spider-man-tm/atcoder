#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i=0; i<n; i++) {
        cin >> p.at(i);
    }

    int ans = 0;
    for (int i=0; i<n-2; i++) {
        if (p.at(i+1) != min(min(p.at(i), p.at(i+1)), p.at(i+2)) && 
            p.at(i+1) != max(max(p.at(i), p.at(i+1)), p.at(i+2))) {
                ans++;
            }
    }
    cout << ans << endl;
}