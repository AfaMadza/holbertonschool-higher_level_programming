#!/usr/bin/node

const request = require('request');
let url = process.argv[2];

let newDict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    let todos = body;
    for (let todo in todos) {
      let userID = todos[todo].userId;
      if (todos[todo].completed) {
        if (newDict[userID] === undefined) {
          newDict[userID] = 1;
        } else {
          newDict[userID] += 1;
        }
      }
    }
  }
  console.log(newDict);
});
