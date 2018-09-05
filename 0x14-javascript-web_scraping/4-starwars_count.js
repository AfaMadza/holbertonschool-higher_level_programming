#!/usr/bin/node

const request = require('request');
let url = process.argv[2];
let character = 'https://swapi.co/api/people/18/';
let count = 0;

request.get(url, function (error, response, body) {
  body = JSON.parse(body);
  if (error) {
    console.log(error);
  }
  let results = body.results;
  for (let result in results) {
    let characters = results[result].characters;
    for (let person in characters) {
      if (characters[person] === character) {
        count += 1;
      }
    }
  }
  console.log(count);
});
