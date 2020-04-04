#include <bits/stdc++.h>
using namespace std;
    
int main() {
    int n, a, b;
    cin >> n >> a >> b;
    int p1 = n * a;
    int p2 = b;
    cout << min(p1, p2) << endl;
}