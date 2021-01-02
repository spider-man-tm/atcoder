function Main(input) {
  inp = input.split("\n");
  let v = inp[1].split(" ").map(n => parseInt(n));
  v = v.sort((a, b) => a - b);
  let ans = v[0];
  for (let i = 1; i < v.length; i++) {
    ans += v[i];
    ans /= 2;
  }
  console.log(ans);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));