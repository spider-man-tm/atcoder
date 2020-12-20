function Main(input) {
  // input = input.split("\n")
  let rgb = input.split(" ").join("");
  rgb = parseInt(rgb);

	if (rgb % 4 === 0) {
    console.log("YES");
  } else {
    console.log("NO");
  };
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));