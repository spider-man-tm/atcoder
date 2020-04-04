#include <bits/stdc++.h>
using namespace std;

int main() {
    string a;
    cin >> a;

    if (a.at(0) != 'a' || a.size() > 1) {
        cout << 'a' << endl;
    } else {
        cout << -1 << endl;
    }
}