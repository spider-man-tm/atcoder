#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, k;
    cin >> a >> b >> c >> k;
    if (a == max(a, max(b, c))) {
        cout << a * pow(2, k) + b + c << endl;
    } else if (b == max(a, max(b, c))) {
        cout << b * pow(2, k) + a + c << endl;
    } else {
        cout << c * pow(2, k) + b + a << endl;
    }
}