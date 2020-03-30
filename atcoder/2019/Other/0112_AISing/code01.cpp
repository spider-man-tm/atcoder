#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, h, w;
    cin >> n >> h >> w;
    int hh, ww;
    hh = n+1-h;
    ww = n+1-w;
    cout << hh*ww << endl;
}