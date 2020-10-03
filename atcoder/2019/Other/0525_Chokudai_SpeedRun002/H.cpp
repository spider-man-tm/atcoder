#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int A, B;
        cin >> A >> B;
        if (A == B) cout << -1 << endl;
        else cout << abs(A - B) << endl;
    }
}