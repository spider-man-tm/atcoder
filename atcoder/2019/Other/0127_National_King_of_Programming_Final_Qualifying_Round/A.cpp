#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, B;
    cin >> N >> A >> B;
    int maxi = min(A, B);
    int mini = max(B-(N-A), 0);
    cout << maxi << " " << mini << endl;

    return 0;
}