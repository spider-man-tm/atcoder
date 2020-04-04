#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    vector<int> ans(3);
    ans.at(a-1) = 1;
    ans.at(b-1) = 1;

    for (int i=0; i<3; i++) {
        if (ans.at(i) == 0) {
            cout << i+1 << endl;
        }
    }
}