#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i=0; i<n; i++) {
        cin >> a.at(i);
    }
    sort(a.begin(), a.end());
    cout << a.at(n-1) - a.at(0) << endl;
}