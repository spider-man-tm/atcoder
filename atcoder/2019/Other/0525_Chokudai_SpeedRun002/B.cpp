#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;

    for (long long i = 0; i < N; i++) {
        long long A, B;
        cin >> A >> B;
        cout << A % B << endl;
    }
}