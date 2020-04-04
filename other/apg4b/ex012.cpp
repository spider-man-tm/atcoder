#include <bits/stdc++.h>
using namespace std;

int main() {
    int ans=1;
    string s;
    cin >> s;
    for (int i=0; i<s.size(); i++) {
        if (i%2==1) {
            char kigou;
            kigou = s.at(i);
            if (kigou=='+') ans++;
            else ans--;
        }
    }
    cout << ans << endl;
}