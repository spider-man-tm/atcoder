#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A;
    cin >> N >> A;
    for (int i=0; i<N; i++) {
        string k;
        int n;
        cin >> k >> n;
        if (k=="/" && n==0) {
            cout << "error" << endl;
            break;
        }
        if (k=="+") {
            A += n;
        } else if (k=="-") {
            A -= n;
        } else if (k=="*") {
            A *= n;
        } else {
            A /= n;
        }
        cout << i+1 << ":" << A << endl;
    }
}