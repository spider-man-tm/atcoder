#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    for (int i=0; i<13; i++) {
        if (i<4) {
            cout << s.at(i);
        } 
        else if (i==4) {
            cout << " ";
        }
        else {
            cout << s.at(i-1);
        }
    }
    cout << endl;
}