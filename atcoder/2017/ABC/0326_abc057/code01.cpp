#include <bits/stdc++.h>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    int ans = A+B;
    if (ans>=24) {
        cout << ans-24 << endl;
    } else {
        cout << ans << endl;
    }
}