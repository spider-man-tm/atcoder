#include <bits/stdc++.h>
using namespace std;

int main() {
    long long l, h;
    int n;
    cin >> l >> h >> n;
    
    for (int i=0; i<n; i++) {
        long long a;
        cin >> a;

        if (a<l) {
            cout << (l-a) << endl;
        } 
        else if (a>h) {
            cout << -1 << endl;
        }
        else {
            cout << 0 << endl;
        }
    }
}