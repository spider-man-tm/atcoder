#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int leng = s.size();

    for (int i=0; i<leng; i++) {
        if (i == leng-1) {
            cout << 'x' << endl;
        } else {
            cout << 'x';
        }
    }
}