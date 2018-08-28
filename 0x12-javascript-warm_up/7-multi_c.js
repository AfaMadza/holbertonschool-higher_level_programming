#!/usr/bin/node

function printStr () {
  let myStr = 'C is fun';
  let myErr = 'Missing number of occurrences';
  if (process.argv[2] === undefined) console.log(myErr);
  for (let i = 0, size = process.argv[2]; i < size; i++) {
    console.log(myStr);
  }
}
printStr();
