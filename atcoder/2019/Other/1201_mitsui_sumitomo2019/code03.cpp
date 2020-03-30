#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;
    int ans = 0;
    int kijun = x/100;
    int amari = x%100;
    if (kijun*5 >= amari) {
        ans = 1;
    }
    cout << ans << endl;
}