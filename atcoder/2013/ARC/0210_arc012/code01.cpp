#include <bits/stdc++.h>
using namespace std;

int main() {
    string day;
    cin >> day;
    if (day=="Sunday" || day=="Saturday") {
        cout << 0 << endl;
    }
    else if (day=="Monday") {
        cout << 5 << endl;
    }
    else if (day=="Tuesday") {
        cout << 4 << endl;
    }
    else if (day=="Wednesday") {
        cout << 3 << endl;
    }
    else if (day=="Thursday") {
        cout << 2 << endl;
    }
    else {
        cout << 1 << endl;
    }
}
