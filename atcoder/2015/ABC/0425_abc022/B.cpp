#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, ans;
    cin >> n;
    vector<long long> a(100001);

    for (long long i=0; i<n; i++) {
        long long tmp;
        cin >> tmp;
        if (a.at(tmp)>0) ans++;
        a.at(tmp)++;
    }

    cout << ans << endl;
}