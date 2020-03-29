#include <bits/stdc++.h>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    int ans = (W-1)*H + (H-1)*W;
    cout << ans << endl;
}