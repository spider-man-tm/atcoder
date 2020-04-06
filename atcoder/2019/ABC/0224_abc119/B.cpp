#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    float ans;
    for (int i=0; i<n; i++) {
        float x;
        string u;
        cin >> x >> u;
        if (u=="JPY") {
            ans += x;
        } else {
            ans += x*380000.0;
        }
    }
    cout << ans << endl;
}