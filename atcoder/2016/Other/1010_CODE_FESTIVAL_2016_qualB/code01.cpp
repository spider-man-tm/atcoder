#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    string T = "CODEFESTIVAL2016";
    int ans;
    for (int i=0; i<16; i++) {
        if (S.at(i) != T.at(i)) ans++;
    }
    cout << ans << endl;
}