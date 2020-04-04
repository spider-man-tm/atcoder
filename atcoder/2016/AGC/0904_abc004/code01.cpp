#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A, B, C;
    cin >> A >> B >> C;
    if (A%2==0 || B%2==0 || C%2==0) {
        cout << 0 << endl;
    } else {
        cout << min({A*B, B*C, C*A}) << endl;
    }
}