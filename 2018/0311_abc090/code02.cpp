#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, ans;
    cin >> a >> b;
    for (int i=a; i<b+1; i++) {
        if (i%10 == i/10000 && i%100/10 == i/1000%10) ans++;
    }
    cout << ans << endl;
}