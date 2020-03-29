#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a;
    b = a / 100;
    c = (a - b * 100) / 10;
    d = a - (b * 100) - (c * 10);
    cout << b + c + d << endl;
}