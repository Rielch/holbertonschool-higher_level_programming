#!/usr/bin/node
const len = process.argv.length;
if (len === 2 || len === 3) {
  console.log(0);
} else {
  const prev = process.argv;
  prev.sort(function (a, b) {
    return (a - b);
  });
  console.log(prev[prev.length - 2]);
}
