#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, d, ans;
    cin >> n >> d;

    int one = d*2+1;
    
    if (n%one==0) {
        ans = n/one;
    } else {
        ans = n/one + 1;
    }
    cout << ans << endl;
}