function Main(input) {
  inp = input.split("\n")
  let N = parseInt(inp[0]);
  let A = parseInt(inp[1]);
  if (N % 500 <= A) {
    console.log("Yes");
  } else {
    console.log("No");
  };
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));