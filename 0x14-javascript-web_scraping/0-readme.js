#!/usr/bin/node

const fs = require('fs');
const f = process.argv[2];

fs.readFile(f, 'utf8', function (error, content) {
  if (error) {
    console.log(error);
  } else {
    console.log(content)
  }
});
