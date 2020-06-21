#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, ans;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int tmp;
        cin >> tmp;
        ans += max(0, 80-tmp);
    }
    cout << ans << endl;
}