#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, countmin, count;
    cin >> n;
    countmin = 999;
    count = 0;

    for (int i=0; i<n; i++) {
        cin >> a;
        count = 0;
        while (a%2==0) {
            a /= 2;
            count++;
        }
        if (count<countmin) countmin = count;
    }
    cout << countmin << endl;
}