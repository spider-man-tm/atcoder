function Main(input) {
  inp = input.split("\n")
  let S = inp[0];
  let ans = S.length;
  while (true) {
    ans -= 2;
    let s1 = S.slice(0, Math.floor(ans/2));
    let s2 = S.slice(Math.floor(ans/2), ans);
    if (s1 === s2) break;
  }
  console.log(ans);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));