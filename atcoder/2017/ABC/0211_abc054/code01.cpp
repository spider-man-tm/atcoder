#include <bits/stdc++.h>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    if (A==1) A=14;
    if (B==1) B=14;

    if (A>B) {
        cout << "Alice" << endl;
    }
    else if (B>A) {
        cout << "Bob" << endl;
    }
    else {
        cout << "Draw" << endl;
    }
}