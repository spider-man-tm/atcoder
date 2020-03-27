#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A, K, ans, over;
    cin >> A >> K;
    over = pow(10, 12) * 2;

    if (K==0) {
        cout << over-A << endl;
    }

    else {
        while (A<over) {
            A += A*K+1;
            ans++;
        }
        cout << ans << endl;
    }
}