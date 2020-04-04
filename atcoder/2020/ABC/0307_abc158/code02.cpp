#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, a, b;
    cin >> n >> a >> b;

    long long block = a+b;
    long long block_n = n/block;
    long long amari = n%block;
    long long ans = 0;

    if (amari >= a) {
        ans = (block_n+1) * a;
    } else {
        ans = block_n * a + amari;
    }

    cout << ans << endl;
}