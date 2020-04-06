#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k, num;
    cin >> n >> k;
    num = 1;
    for (int i=0; i<n; i++) {
        if (num<k) num *= 2;
        else num += k;
    }
    cout << num << endl;
}