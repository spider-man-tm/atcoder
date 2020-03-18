#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, ans;
    cin >> a >> b;
    if (a>=13) {
        ans = b;
    } else if (a<6) {
        ans = 0;
    } else {
        ans = b/2;
    }
    cout << ans << endl;
}