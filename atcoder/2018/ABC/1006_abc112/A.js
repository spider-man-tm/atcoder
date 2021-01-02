function Main(input) {
  inp = input.split("\n")
  if (parseInt(inp[0]) === 1) {
    console.log("Hello World");
  } else {
    let A = parseInt(inp[1]);
    let B = parseInt(inp[2]);
    console.log(A + B);
  }
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));