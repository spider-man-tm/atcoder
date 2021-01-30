function Main(input) {
  let inp = input.split("\n");
  let [S, W] = inp[0].split(" ");
  S = Number(S);
  W = Number(W);
  if (W >= S) {
    console.log("unsafe");
  } else {
    console.log("safe");
  }
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));