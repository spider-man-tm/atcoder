#include <bits/stdc++.h>
using namespace std;

int main() {
    int y;
    cin >> y;
    if (y%400==0) {
        cout << "YES" << endl;
    } else if (y%100==0) {
        cout << "NO" << endl;
    } else if (y%4==0) {
        cout << "YES" << endl;
    } else {
        cout <<"NO" << endl;
    }
}