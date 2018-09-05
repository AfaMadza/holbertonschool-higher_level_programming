#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const f = process.argv[3];
let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (body) {
    body = JSON.stringify(body);
    fs.writeFile(f, body, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
