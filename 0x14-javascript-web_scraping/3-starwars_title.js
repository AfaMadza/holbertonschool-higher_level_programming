#!/usr/bin/node

const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (body) {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
