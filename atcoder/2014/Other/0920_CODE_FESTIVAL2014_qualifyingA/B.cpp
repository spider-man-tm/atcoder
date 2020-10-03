#include <bits/stdc++.h>
using namespace std;

int main() {
    string A;
    long long B;
    cin >> A >> B;
    cout << A[(B-1) % A.length()] << endl;
}