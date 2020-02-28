#include <bits/stdc++.h>
using namespace std;

// AからBまでの総和を求める関数: sum_range
int sum_range(int a, int b) {
    // ベースケース
    if (a==b) {
        return a;
    }
    // 再帰ステップ
    return sum_range(a, b-1) + b;
}


// (補助関数)
int array_sum_from_i(vector<int> &data, int i) {
    // ベースケース
    if (i==data.size()) return 0;  // 対象の要素がないので総和は0

    // 再帰ステップ
    int s = array_sum_from_i(data, i+1);  // i+1番目以降の要素の総和
    return data.at(i) + s;  // 「i番目以降の要素の総和」=「i番目の要素」+ s
}

// 配列の要素の総和
int sum_array(vector<int> &data) {
    return array_sum_from_i(data, 0);
}


// (補助関数)  i ~ N-1の範囲にNの約数が存在するか
bool has_divisor(int N, int i) {
    // ベースケース1
    if (i==N) {
        // そもそも対象となる整数が無いのでfalse
        return false;
    }
    // ベースケース2
    if (N%i==0) {
        // 実際にiはNの約数なので、i ~ N-1の間に約数が存在する
        return true;
    }

    // 再帰ステップ
    // i+1 ~ N-1の範囲の結果がi ~ N-1の範囲の結果となる
    // (ベースケース2によって、iがNの約数の場合は取り除かれているので、あとはi+1 ~ N-1の範囲を調べればよい)
  return has_divisor(N, i + 1);
}

bool is_prime(int N) {
    if (N == 1) {
        // 1は素数ではない
        return false;
    }
    else if (N == 2) {
        // 2は素数
        return true;
    }
    else {
        // 2~(N-1)の範囲に約数が無ければ、Nは素数
        return !has_divisor(N, 2);
    }
}


// dataのi番目以降の要素を逆順にした配列を返す
vector<int> reverse_array_from_i(vector<int> &data, int i) {
    // ベースケース
    if (i == data.size()) {
        vector<int> empty_array(0);  // 要素数0の配列
        return empty_array;
    }
    
    // 再帰ステップ
    vector<int> tmp = reverse_array_from_i(data, i + 1);  // dataのi+1番目以降の要素を逆順にした配列を得る
    tmp.push_back(data.at(i));  // 末尾にdataのi番目の要素を追加
    return tmp;
}
 
// 配列を逆順にしたものを返す
vector<int> reverse_array(vector<int> &data) {
    return reverse_array_from_i(data, 0);
}


int main() {
    cout << sum_range(2, 5) << endl; // 14
    cout << sum_range(-1, 3) << endl; // 5
    vector<int> a = {0, 3, 9, 1, 5};
    cout << sum_array(a) << endl; // 18
    cout << is_prime(12) << endl; // 0
    cout << is_prime(13) << endl; // 1
    cout << endl;
    vector<int> b = reverse_array(a);
    for (int i = 0; i < b.size(); i++) {
        cout << b.at(i) << endl;  // 5 1 9 3 0
  }
}