#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    bool flag = false;
    bool ans = false;
    for (int i=0; i<S.size(); i++) {
        char c = S[i];
        if (flag==false) {
            if (c=='C') flag = true;
            continue;
        }
        if (flag) {
            if (c=='F') {
                cout << "Yes" << endl;
                return 0;
            }
        }
    }
    cout << "No" << endl;
    return 0;
}