#include <bits/stdc++.h>
using namespace std;

int main() {
    double Height, BMI;
    cin >> Height >> BMI;
    double ans = pow(Height/100.0, 2) * BMI;
    cout << ans << endl;

    return 0;
}