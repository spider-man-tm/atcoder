#include <bits/stdc++.h>
using namespace std;

int main() {
    string date;
    cin >> date;
    string year = date.substr(0, 4);
    string month = date.substr(5, 2);
    string day = date.substr(8, 2);

    int year_n = atoi(year.c_str());
    int month_n = atoi(month.c_str());
    int day_n = atoi(day.c_str());

    bool heisei = true;

    if (year_n>2019) {
        heisei = false;
    }
    else {
        if (month_n > 4) {
            heisei = false;
        }
    }
    if (heisei) {
        cout << "Heisei" << endl;
    }
    else {
        cout << "TBD" << endl;
    }
}