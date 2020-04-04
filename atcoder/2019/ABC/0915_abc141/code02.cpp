#include <bits/stdc++.h>
using namespace std;

int main() {
    string ss;
    cin >> ss;
    string ans = "Yes";

    for (int i=0; i<ss.size(); i++) {
        if (i%2==1) {
            if (ss.at(i) == 'R') {
                ans = "No";
                break;
            }
        }
        else {
            if (ss.at(i) == 'L') {
                ans = "No";
                break;
            }
        }
    }
    cout << ans << endl;
}