#include <bits/stdc++.h>
using namespace std;


int keta(int n) {
    if (n/100 >= 1) {
        return 3;
    }
    else if (n/10 >= 1) {
        return 2;
    }
    else {
        return 1;
    }
}


int main() {
    int a, b;
    cin >> a >> b;
    int k = keta(b);
    int n = a * pow(10, k) + b;

    string ans = "No";
    for (int i=1; i<1000; i++) {
        if (n == (i*i)) {
            ans = "Yes";
        }
    }

    cout << ans << endl;
}