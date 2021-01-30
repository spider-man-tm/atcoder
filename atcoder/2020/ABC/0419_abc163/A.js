function Main(input) {
  let inp = input.split("\n");
  let R = parseInt(inp[0]);
  console.log(2 * R * Math.PI);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));