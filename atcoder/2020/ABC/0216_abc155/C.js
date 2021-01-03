function Main(input) {
  inp = input.split("\n")
  let N = parseInt(inp[0]);
  let ans = {};
  let maximum = 0;
  for (let i = 0; i < N; i++) {
    S = inp[i+1];
    if (ans[S]) {
      ans[S] += 1;
      maximum = Math.max(maximum, ans[S]);
    } else {
      ans[S] = 1;
      maximum = Math.max(maximum, ans[S]);
    }
  }

  let ans2 = [];
  for (let key in ans) {
    let value = ans[key];
    if (value === maximum) {
      ans2.push(key);
    }
  }

  ans2.sort();
  for (let i = 0; i < ans2.length; i++) {
    console.log(ans2[i]);
  }

};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));