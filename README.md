Name: Competitive programming
====

## Directory
### AtCoder
- AC Source code.
- This source code is written by Python or C++.

### AOJ
- AC Source code of Aizu Online Judge.

<br>
<br>

## Version
- Python
    - Python 3.8.2（2020/04/04〜）
    - Python 3.4.3（〜2020/04/04）
- C++
    - GCC 9.2.1（2020/04/04〜）
    - GCC 5.4.1（〜2020/04/04）

<br>
<br>

## アルゴリズム, テクニック

|  Name  |  Problem No  |
| ---- | ---- |
|  二分探索  |  ABC_146 C, ABC_143 D, ABC_036 C, ABC_077 C |
|  DFS（深さ優先探索）  |  ABC_138 D  |
|  BFS（幅優先探索）  |  ABC_007 C, ABC_168 D, ARC_031 B, ABC_146 D |
|  [bit全探索](https://qiita.com/gogotealove/items/11f9e83218926211083a)  |  ABC_147 D, 1stPAST G, ABC_002 C, ABC_128 C, ARC_061_A, ABC_167_C  |
|  DP（動的計画法）  |  ARC_029 A, ABC_129 C, AGC_043 A  |
| 確率DP | ABC_184 D |
|  ダイクストラ  |  ABC_016 C  |
|  ワーシャルフロイド  |  ABC_012 D  |
|  クラスカル法  |    |
|  再帰関数  |  ABC_026 C, ABC_115 D, 2nd_PAST E, ABC_184 D, ABC_115_D |
|  貪欲法  |  ABC_024 C, ABC_161 E, キーエンスプログラミングコンテスト2020 B, CODE_FESTIVAL_2016_qual_A C  |
|  累積和  |  Tenka1_Programmer_Beginner_Contest_2019 C, ABC_122 C, ABC_163 D  |
|  しゃくとり法  |  ABC_038 C, ABC_130 D  |
|  いもす法  |  東京海上日動プログラミングコンテスト2020 C  |

<br>
<br>

## データ構造

|  Name  |  Problem No  |
| ---- | ---- |
|  Union-Find  |  ABC_157 D, ARC_032 B, ABC_075 C  |
|  根付き木  |  ABC_187 E  |
|  二分探索木  |    |
|  グラフ  |    |
|  優先度付きキュー  |  ABC_141 D, 2ndPAST F |
|  キュー  |  ABC_161 D  |

<br>
<br>
<br>

## Remarks
- ある整数 $x$ が、素因数分解によって $x=p^n×q^m× \cdots (p, q, \cdots $は素数)$ と表せる時、$x$ の約数の個数は $(n + 1) × (m + 1) × \cdots $ となる。（素数を使わない時もあるので、+1）
- A, Bの公約数 = GCD(A, B)の約数
- [NIMについて](https://nanikaka.hatenadiary.org/entry/20120524/1337797626)
- 8の倍数 -> 8の倍数下3桁が8の倍数であれば、どんなに大きい数であっても、8の倍数
- [2~13の倍数の色々な判定法まとめ](https://manabi.matiralab.com/times2-13/)
- [Pythonの辞書型の様々なソート方法](https://techacademy.jp/magazine/19309)
- PythonのCounter、クラスにはmost_common()というメソッドがあります。これは(要素, 出現回数)というタプルを出現回数順に並べたリストを返します。
- プログラミングの静的チェックにて、()の位置判定を正しく行うアルゴリズム->（ABC064）
- [パティを重ねる再帰問題 ABC115](https://atcoder.jp/contests/abc115/tasks/abc115_d)
- [-n進数問題](https://atcoder.jp/contests/abc105/tasks/abc105_c)