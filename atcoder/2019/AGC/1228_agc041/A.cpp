#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, A, B;
    cin >> N >> A >> B;
    if ((B-A)%2==0) {
        cout << (B-A)/2 << endl;
    } else {
        long long ans;
        ans = min(A-1, N-B) + 1 + (B-A-1)/2;
        cout << ans << endl;
    }
}