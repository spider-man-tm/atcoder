#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> data = {6, 15, 4, 2, 8, 5, 11, 9, 7, 13};
    int n = 10;
    for (int i=1; i<n; i++) {
        int tmp = data.at(i);
        int j = i-1;
        while (j>=0 && data.at(j) > tmp) {
            data.at(j+1) = data[j];
            j--;
        data.at(j+1) = tmp;
        }
        for (int i=0; i<n; i++) {
            cout << data.at(i) << " ";
        }
        cout << endl;
    }
    cout << endl;
    for (int i=0; i<n; i++) {
        cout << data.at(i) << " ";
    }
}

/*
6 15 4 2 8 5 11 9 7 13 
4 6 15 2 8 5 11 9 7 13 
2 4 6 15 8 5 11 9 7 13 
2 4 6 8 15 5 11 9 7 13 
2 4 5 6 8 15 11 9 7 13 
2 4 5 6 8 11 15 9 7 13 
2 4 5 6 8 9 11 15 7 13 
2 4 5 6 7 8 9 11 15 13 
2 4 5 6 7 8 9 11 13 15 

2 4 5 6 7 8 9 11 13 15 
*/