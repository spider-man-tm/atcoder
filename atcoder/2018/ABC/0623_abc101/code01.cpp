#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int ans = 0;
    for (int i=0; i<4; i++) {
        char c = s.at(i);

        if (c=='+') {
            ans++;
        }
        else {
            ans--;
        }
    }
    cout << ans << endl;
}