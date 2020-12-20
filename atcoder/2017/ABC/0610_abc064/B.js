function Main(input) {
  let inp = input.split("\n");
  let N = parseInt(inp[0])
  let a = inp[1].split(" ").map(n=>parseInt(n));
  a.sort();
  console.log(a[N-1] - a[0]);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));