#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int minn = min(min(a, b), c);
    int maxx = max(max(a, b), c);
    cout << maxx - minn << endl;
}