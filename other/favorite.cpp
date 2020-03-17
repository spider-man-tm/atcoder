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