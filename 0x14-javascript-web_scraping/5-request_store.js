#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const f = process.argv[3];
let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.stringify(body);
    let data = JSON.parse(body);
    fs.writeFile(f, data, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
