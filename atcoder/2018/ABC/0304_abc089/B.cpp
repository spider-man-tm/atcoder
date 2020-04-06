#include <bits/stdc++.h>
using namespace std;

int main () {
    int n;
    string ans = "Three";
    cin >> n;
    for (int i=0; i<n; i++) {
        string k;
        cin >> k;
        if (k=="Y") {
            ans = "Four";
            break;
        }
    }
    cout << ans << endl;
}