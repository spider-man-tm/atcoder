#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, ans;
    cin >> N;
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        if (s=="black") ans++;
        else ans--;
    }
    if (ans>0) cout << "black" << endl;
    else cout << "white" << endl;
}