#include <bits/stdc++.h>
using namespace std;

int main() {
    long long a, b;
    cin >> a >> b;
    if ((b-a)%2==0) {
        cout << abs(b-a)/2 + min(a, b) << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
}