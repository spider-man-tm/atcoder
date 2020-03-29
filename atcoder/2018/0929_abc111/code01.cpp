#include <bits/stdc++.h>
using namespace std;

int main() {
    string n;
    cin >>n;

    for (int i=0; i<3; i++) {
        if (n.at(i)=='1') {
            n.at(i) = '9';
        }
        else if (n.at(i)=='9') {
            n.at(i) = '1';
        }
    }
    int ans = atoi(n.c_str());
    cout << ans << endl;
}