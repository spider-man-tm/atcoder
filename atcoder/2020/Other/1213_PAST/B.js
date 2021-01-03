function Main(input) {
  let inp = input.split("\n");
  let N = parseInt(inp[0]);
  let S = inp[1];
  let T = "";

  for (let i = 0; i < N; i++) {
    tmp = S[i];
    T = T.replace(tmp, "");
    T += tmp;
  }

  console.log(T);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));