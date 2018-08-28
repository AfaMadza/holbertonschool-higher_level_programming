#!/usr/bin/node

function almostMax () {
  if (process.argv.length < 3) return (0);
  let myArr = process.argv;
  let length = process.argv.length;
  myArr.sort();
  return (myArr[length - 2]);
}
console.log(almostMax());
