#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> data(5);
    for (int i=0; i<5; i++) {
        cin >> data.at(i);
    }
    int counter = 0;
    for (int i=0; i<5; i++) {
        if (i==0) counter++;
        else {
            if (data.at(i)==data.at(i-1)) {
                break;
            } else counter++;
        }
    }
    if (counter==5) {
        cout << "NO" << endl;
    } else {
        cout << "YES" << endl;
    }
}