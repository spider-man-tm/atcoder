#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> v = {a, b, c};
    sort(v.begin(), v.end());
    if (v.at(2) == v.at(0)+v.at(1)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}