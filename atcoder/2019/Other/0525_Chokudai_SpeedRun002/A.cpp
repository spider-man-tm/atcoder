#include <bits/stdc++.h>
typedef long long int ll;
using namespace std;

int main() {
    int N;
    cin >> N;
    ll anslist[N];
    
    for (int i = 0; i < N; i++) {
        ll a, b;
        cin >> a >> b;
        anslist[i] = a * b;
    }

    for (int i = 0; i < N; i++) {
        cout << anslist[i] << endl;
    }
}