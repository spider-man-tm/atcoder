#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int mini = 1000;
    for (int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        mini = min(mini, tmp);
    }
    cout << mini << endl;
}