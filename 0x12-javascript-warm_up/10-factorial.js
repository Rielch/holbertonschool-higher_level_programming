#!/usr/bin/node
const a = parseInt(process.argv[2]);
function factorial (a) {
  if (a === 1 || isNaN(a)) {
    return (1);
  }
  a *= factorial(a - 1);
  return (a);
}
console.log(factorial(a));
