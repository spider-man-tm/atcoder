#include <bits/stdc++.h>
using namespace std;

int main()
{
  string s;
  cin >> s;

  for (auto &e : s) {
    if (e == 'O') e = '0';
    else if (e == 'D') e = '0';
    else if (e == 'I') e = '1';
    else if (e == 'Z') e = '2';
    else if (e == 'S') e = '5';
    else if (e == 'B') e = '8';
  }

  cout << s << endl;
}
