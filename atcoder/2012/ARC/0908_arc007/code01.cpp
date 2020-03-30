#include <bits/stdc++.h>
using namespace std;

int main() {
    char X;
    string s;
    cin >> X >> s;
    for (int i=0; i<s.size(); i++) {
        if (s.at(i) != X) {
            cout << s.at(i);
        }
    }
    cout << endl;
}