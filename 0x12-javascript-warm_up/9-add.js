#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
let firNo = Number(process.argv[2]);
let secNo = Number(process.argv[3]);
console.log(add(firNo, secNo));
