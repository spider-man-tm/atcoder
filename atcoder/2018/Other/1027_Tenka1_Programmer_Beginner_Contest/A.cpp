#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    if (S.size()==2) cout << S << endl;
    else cout << S[2] << S[1] << S[0] << endl;
}