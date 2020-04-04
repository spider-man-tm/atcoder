#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int n10 = N/10;
    int n1 = N%10;

    if (n1<=6) {
        cout << n10*100 + n1*15 << endl;
    } else {
        cout << (n10+1)*100 << endl;
    }
}