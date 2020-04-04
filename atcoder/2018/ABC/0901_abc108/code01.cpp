#include <bits/stdc++.h>
using namespace std;

int main() {
    int k;
    cin >> k;
    int odd, eve;
    if (k%2==0) {
        odd = k/2;
        eve = k/2;
    } else {
        odd = k/2 + 1;
        eve = k/2;
    }
    cout << odd * eve << endl;
}