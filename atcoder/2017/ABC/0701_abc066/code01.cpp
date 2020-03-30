#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v(3);
    cin >> v.at(0) >> v.at(1) >> v.at(2);
    sort(v.begin(), v.end());
    cout << v.at(0) + v.at(1) << endl;
}