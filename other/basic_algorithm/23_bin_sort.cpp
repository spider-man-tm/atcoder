#include <bits/stdc++.h>
using namespace std;


int bin_sort(vector<int> data) {
    vector<int> arr = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int length = data.size();

    for (int i=0; i<length; i++) {
        int no = data.at(i);
        arr.at(no)++;
    }

    for (int i=0; i<10; i++) {
        int n = arr.at(i);

        if (n>0) {
            for (int j=0; j<n; j++) {
                cout << i << " ";
            }
        }
    }
}


int main() {
    vector<int> data = {
        3, 4, 1, 8, 8, 0, 3, 8, 9, 3, 2, 7, 4, 5
        };
    bin_sort(data);
}