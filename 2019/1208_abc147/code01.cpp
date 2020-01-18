#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int su = a+b+c;
    if (su>=22) {
        cout << "bust" << endl;
    }
    else {
        cout << "win" << endl;
    }
}