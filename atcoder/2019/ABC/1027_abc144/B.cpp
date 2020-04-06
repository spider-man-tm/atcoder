#include <bits/stdc++.h>
using namespace std;

int main () {
    int n;
    bool flag = false;
    cin >> n;
    for (int i=1; i<10; i++) {
        for (int j=1; j<10; j++) {
            if (i*j==n) {
                flag = true;
                break;
            }
        if (flag==true) {
            break;
        }
        }
    }
    if (flag==true) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}