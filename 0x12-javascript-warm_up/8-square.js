#!/usr/bin/node

function printSq () {
  let prompt = 'X';
  let size = parseInt(Number(process.argv[2]));
  if (isNaN(size) === true) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < size; i++) {
      console.log(prompt.repeat(size));
    }
  }
}
printSq();
