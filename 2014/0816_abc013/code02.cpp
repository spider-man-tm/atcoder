#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, ans;
    cin >> a >> b;

    if (a<=b) {
        ans = min(b-a, a+(10-b));
    } else {
        ans = min(a-b, b+(10-a));
    }

    cout << ans << endl;
}