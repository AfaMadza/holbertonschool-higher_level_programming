#!/usr/bin/node

function printNum () {
  if (isNaN(process.argv[2]) === true) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + parseInt(Number(process.argv[2])));
  }
}
printNum();
