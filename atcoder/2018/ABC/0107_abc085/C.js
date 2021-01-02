function Main(input) {
  inp = input.split("\n")
  let [N, Y] = inp[0].split(" ").map(n => parseInt(n));
  
  for (let i = 0; i < N+1; i++) {
    for (let j = 0; j < N+1-i; j++) {
      let k = N - i - j;
      if (10000*i + 5000*j + 1000*k === Y) {
        console.log(i, j, k);
        return;
      }
    }
  }

  console.log(-1, -1, -1);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));