#include <bits/stdc++.h>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    if (a.size()==b.size()) {
        for (int i=0; i<a.size(); i++) {
            cout << a.at(i) << b.at(i);
        }
        cout << endl;
    }
    else {
        for (int i=0; i<b.size(); i++) {
            cout << a.at(i) << b.at(i);
        }
        cout << a.at(a.size()-1) << endl;
    }
}