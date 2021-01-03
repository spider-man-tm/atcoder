function Main(input) {
  let S = input.split("\n")[0];
  let searchO = S.indexOf("ooo");
  let searchX = S.indexOf("xxx");

  if (searchO !== -1) {
    console.log("o");
  } else if (searchX !== -1) {
    console.log("x");
  } else {
    console.log("draw");
  }
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));