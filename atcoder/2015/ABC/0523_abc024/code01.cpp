#include <bits/stdc++.h>
using namespace std;

int main( ) {
    int a, b, c, k, s, t;
    cin >> a >> b >> c >> k >> s >> t;
    int total = a*s + b*t;
    if (s+t>=k) total -= (s+t)*c;
    cout << total << endl;
}