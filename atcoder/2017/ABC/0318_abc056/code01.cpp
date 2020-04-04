#include <bits/stdc++.h>
using namespace std;

int main() {
    char a, b;
    cin >> a >> b;

    if (a == 'D') {
        if (b == 'H') {
            b = 'D';
        } else {
            b = 'H';
        }
    }

    cout << b << endl;
}