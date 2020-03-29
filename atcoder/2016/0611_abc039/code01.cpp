#include <bits/stdc++.h>
using namespace std;

main() {
    int a, b, c;
    cin >> a >> b >> c;
    int ans = 2*a*b + 2*b*c + 2*c*a;
    cout << ans << endl;
}