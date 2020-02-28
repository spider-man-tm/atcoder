#include <bits/stdc++.h>
using namespace std;


int main() {
    vector<int> data = {6, 15, 4, 2, 8, 5, 11, 9, 7, 13};
    int n = 10;
    for (int i=0; i<n; i++) {
        int min = i;
        for (int j=i+1; j<n; j++) {
            if (data.at(min) > data.at(j)) min=j;
        }

        int tmp = data.at(i);
        int tmp2 = data.at(min);
        data.at(i) = tmp2;
        data.at(min) = tmp;
    }

    for (int i=0; i<n; i++) {
        cout << data.at(i) << " ";
    }
}