#include <bits/stdc++.h>
using namespace std;

int main() {
  long long n, m;
  cin >> n >> m;

  if (n>=2 && m>=2) {
      cout << n*m - (n-2)*2 - (m-2)*2 - 4 << endl;
  }
  else if (n==1 && m==1) {
      cout << 1 << endl;
  }
  else if (n==1 && m>=2) {
      cout << m-2 << endl;
  }
  else {
      cout << n-2 << endl;
  }
  return 0;
}