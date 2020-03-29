#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n==25) {
        cout << "Christmas" << endl;
    } else if (n==24) {
        cout << "Christmas Eve" << endl;
    } else if (n==23) {
        cout << "Christmas Eve Eve" << endl;
    } else {
        cout << "Christmas Eve Eve Eve" << endl;
    }
}