#include <bits/stdc++.h>
using namespace std;

int group(int n) {
    if (n==2) {
        return 0;
    }
    else if (n==4 || n==6 || n==9 || n==11) {
        return 1;
    }
    else {
        return 2;
    }
}


int main() {
    int x, y;
    cin >> x >> y;
    int xx = group(x);
    int yy = group(y);
    if (xx==yy) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}