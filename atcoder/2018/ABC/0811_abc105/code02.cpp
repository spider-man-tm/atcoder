#include <bits/stdc++.h>
using namespace std;

int main() {
    string ans = "No";
    int n;
    cin >> n;
    for (int i=0; i<30; i++) {
        for (int j=0; j<15; j++) {
            int place = i*4 + j*7;
            if (place == n) {
                ans = "Yes";
            }
        }
    }
    cout << ans << endl;
}