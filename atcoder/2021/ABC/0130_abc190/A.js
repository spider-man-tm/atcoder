function Main(input) {
  let inp = input.split("\n");
  let [A, B, C] = inp[0].split(" ");
  A = Number(A);
  B = Number(B);
  C = Number(C);
  
  if (C === 0) {
    if (A > B) {
      console.log("Takahashi");
    } else {
      console.log("Aoki");
    }
  } else {
    if (B > A) {
      console.log("Aoki");
    } else {
      console.log("Takahashi");
    }
  }
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));