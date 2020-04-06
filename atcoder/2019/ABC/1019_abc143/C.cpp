#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    string ss;
    cin >> n >> ss;
    int ans = 1;
    char s_before = ss[0];
    for (int i=0; i<n; i++) {
        char s = ss[i];
        if (s != s_before) {
            ans++;
            s_before = s;
        }
    }
    cout << ans << endl;
}