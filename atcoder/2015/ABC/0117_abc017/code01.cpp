#include <bits/stdc++.h>
using namespace std;

int main() {
    int s1, s2, s3, e1, e2, e3;
    cin >> s1 >> e1 >> s2 >> e2 >> s3 >> e3;

    float a = s1 * e1 / 10;
    float b = s2 * e2 / 10;
    float c = s3 * e3 / 10;
    float total = a+b+c;
    int t = total;

    cout << t << endl;
}