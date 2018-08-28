#!/usr/bin/node

function printVal () {
  if (process.argv[2] === undefined) {
    console.log('No argument');
  } else {
    console.log(process.argv[2]);
  }
}
printVal();
