#!/usr/bin/node

function factorial (n) {
  if (n === 0) return (1);
  return (n * factorial(n - 1));
}
let firNo = isNaN(Number(process.argv[2])) ? 1 : Number(process.argv[2]);
console.log(factorial(firNo));
