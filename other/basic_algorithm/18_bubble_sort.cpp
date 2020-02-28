#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> data = {6, 15, 4, 2, 8, 5, 11, 9, 7, 13};
    bool change = true;
    int n = 10;
    for (int i=0; i<n; i++) {
        if (change==false) break;
        change = false;
        for (int j=0; j<n-i-1; j++) {
            if (data.at(j) > data.at(j+1)) {
                int tmp1 = data.at(j), tmp2 = data.at(j+1);
                data.at(j) = tmp2;
                data.at(j+1) = tmp1;
                change = true;
            }
        }
    }
    for (int i=0; i<n; i++) {
        cout << data.at(i) << " ";
    }
}

/*
data:  [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
data:  [6, 4, 2, 8, 5, 11, 9, 7, 13, 15]
data:  [4, 2, 6, 5, 8, 9, 7, 11, 13, 15]
data:  [2, 4, 5, 6, 8, 7, 9, 11, 13, 15]
data:  [2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
data:  [2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
[2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
*/