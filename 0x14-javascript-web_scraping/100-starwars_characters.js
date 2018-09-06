#!/usr/bin/node

const request = require('request');
let url = 'https://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    let characters = body.characters;
    for (let character in characters) {
      let person = characters[character];
      request(person, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          body = JSON.parse(body);
          let name = body.name;
          console.log(name);
        }
      });
    }
  }
});
