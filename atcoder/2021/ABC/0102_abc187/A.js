function Main(input) {
  let inp = input.split("\n")[0].split(" ");
  let A = inp[0];
  let B = inp[1];
  let a = Number(A[0]) + Number(A[1]) + Number(A[2]);
  let b = Number(B[0]) + Number(B[1]) + Number(B[2]);
  console.log(Math.max(a, b));
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));