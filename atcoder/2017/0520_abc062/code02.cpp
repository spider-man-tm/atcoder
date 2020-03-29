#include <bits/stdc++.h>
using namespace std;

int main() {
    int h, w;
    cin >> h >> w;
    string bar(w+2, '#'), tmp;
    cout << bar << endl;
    for (int i=0; i<h; i++) {
        cin >> tmp;
        cout << '#' << tmp << '#' << endl;
    }
    cout << bar << endl;
}