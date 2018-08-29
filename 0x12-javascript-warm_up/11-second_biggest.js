#!/usr/bin/node

function almostMax () {
  if (process.argv.length < 2) return (0);
  let myArr = process.argv.slice(2).map(x => Number(x));
  return (myArr.sort().reverse()[1]);
}
console.log(almostMax());
