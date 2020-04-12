#include <bits/stdc++.h>
using namespace std;

int main() {
    int h, m;
    cin >> h >> m;
    int ans_m = 60 - m;
    int ans_h = (17 - h) * 60;
    cout << ans_m + ans_h << endl;
}