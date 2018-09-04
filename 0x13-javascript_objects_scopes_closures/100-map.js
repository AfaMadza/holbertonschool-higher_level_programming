#!/usr/bin/node
const list = require('./100-data').list;

function mapArray (list) {
  let newArray = list.map((n, i) =>
    n * i);
  console.log(list);
  console.log(newArray);
}
mapArray(list);
