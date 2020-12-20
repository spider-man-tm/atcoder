function Main(inp) {
  let input = inp.split("\n");
  let N = parseInt(input[0]);
  let S = input[1];
  let l = 0;
  let r = 0;
  for (var i = 0; i < N; i++) {
    if (S[i] === "(") {
      r += 1;
    } else if (r) {
      r -= 1;
    } else {
      l += 1;
    }
  };
  let ans = "(".repeat(l) + S + ")".repeat(r);
  console.log(ans);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));