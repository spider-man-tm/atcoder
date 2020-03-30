#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> nn(n);
    for (int i=0; i<m; i++) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        nn.at(tmp1-1) += 1;
        nn.at(tmp2-1) += 1;
    }
    for (int i=0; i<n; i++) {
        cout << nn.at(i) << endl;
    }
}