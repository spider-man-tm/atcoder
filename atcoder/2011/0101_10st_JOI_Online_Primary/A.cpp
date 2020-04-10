#include <bits/stdc++.h>
using namespace std;

int main() {
    int l1, l2, l3, l4;
    cin >> l1 >> l2 >> l3 >> l4;
    int total = l1 + l2 + l3 + l4;
    int x = total/60;
    int y = total%60;
    cout << x << endl << y << endl;

    return 0;
}