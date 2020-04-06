#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, max_ans;
    cin >> n;
    vector<string> s(n);
    for (int i=0; i<n; i++) {
        cin >> s.at(i);
    }    
    cin >> m;
    vector<string> t(m);
    for (int i=0; i<m; i++) {
        cin >> t.at(i);
    }
    max_ans = 0;

    for (int i=0; i<n; i++) {
        string tmp;
        tmp = s.at(i);
        int tmp_ans = 0;
        for (int i=0; i<n; i++) {
            if (s.at(i)==tmp) tmp_ans++;
        }
        for (int i=0; i<m; i++) {
            if (t.at(i)==tmp) tmp_ans--;
        }
        if (tmp_ans > max_ans) max_ans = tmp_ans;
    }
    cout << max_ans << endl;
}