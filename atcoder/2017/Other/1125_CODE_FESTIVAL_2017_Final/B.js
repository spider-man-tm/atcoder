function Main(input) {
  inp = input.split("\n")
  // 整数の入力
  let S = inp[0];
  let dic = {
    'a': 0, 'b': 0, 'c': 0
  };
  for (let i = 0; i < S.length; i++) {
    dic[S.charAt(i)] += 1;
  }
  let l = [dic.a, dic.b, dic.c];
  if (Math.max(...l) - Math.min(...l) > 1) {
    console.log("NO");
  } else {
    console.log("YES");
  }
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));