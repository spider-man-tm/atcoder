#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int ans, ball;
    for (int i=0; i<n; i++) {
        cin >> ball;
        if (abs(k-ball) > ball) {
            ans += ball*2;
        } else {
            ans += abs(k-ball)*2;
        }
    }
    cout << ans << endl;
}