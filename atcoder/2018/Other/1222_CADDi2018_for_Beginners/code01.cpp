#include <bits/stdc++.h>
using namespace std;

int main() {
    string n;
    cin >> n;
    int ans;

    for (int i=0; i<4; i++) {
        if (n.at(i) == '2') ans++;
    }
    cout << ans << endl;
}