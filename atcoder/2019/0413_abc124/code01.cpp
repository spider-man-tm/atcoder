#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, cnt;
    cin >> a >> b;

    if (max(a, b)==a) {
        cnt += a;
        a--;
    } else {
        cnt += b;
        b--;
    }

    cnt += max(a, b);

    cout << cnt << endl;
}