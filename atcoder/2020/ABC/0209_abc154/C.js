function Main(input) {
  let inp = input.split("\n");
  let N = parseInt(inp[0]);
  let A = inp[1].split(" ").map(n => parseInt(n));
  let Aset = new Set(A);
  
  if (Aset.size === N) {
    console.log("YES");
  } else {
    console.log("NO");
  }
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));