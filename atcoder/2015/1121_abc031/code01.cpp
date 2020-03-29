#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, d;
    cin >> a >> d;
    if (d < a) {
        d++;
    } else {
        a++;
    }
    cout << a*d << endl;
}