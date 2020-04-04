// stringからintに型変換
int main() {
    std::string numStr = "1234";
    int num = atoi(numStr.c_str());
    printf("数値：%d\n", num);
    return 0;
}


// intからstringに型変換
int main() {
    std::string str;
    int num = 4321;
    str = std::to_string(num);
    printf("数値：%s\n", str.c_str());
    return 0;
}


// 確率Pで成功する事象を繰り返した時、
// 初めて成功するまでに挑戦する回数の期待値
// 1/p  つまりサイコロで1が出るまでに挑戦する回数の期待値は6