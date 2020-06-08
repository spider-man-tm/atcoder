#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, B, ans;
    cin >> N >> A >> B;

    if (N<=5) {
        ans = B*N;
    } else {
        ans = B*5 + A*(N-5);
    }
    cout << ans << endl;
    return 0;
}