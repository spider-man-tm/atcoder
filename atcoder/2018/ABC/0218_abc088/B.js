function Main(input) {
  inp = input.split("\n")
  let a = inp[1].split(" ").map(n=>parseInt(n));
  a = a.sort((a, b) => b - a);
  let Alice = 0;
  let Bob = 0;
  for (i=0; i<a.length; i++) {
    if (i % 2 === 0) {
      Alice += a[i];
    } else {
      Bob += a[i];
    }
  };
  console.log(Alice - Bob);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));