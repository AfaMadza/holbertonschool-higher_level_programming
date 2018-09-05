#!/usr/bin/node
const dict = require('./101-data').dict;

function organizeDict (dict) {
  let obj = {};
  let valueList = [];
  let newKeys = Object.keys(dict).map(function (key) {
    return dict[key];
  })
    .filter(function (elem, index, self) {
      return index === self.indexOf(elem);
    });
  for (let i = 0; i < newKeys.length; i++) {
    for (let key in dict) {
      if (newKeys[i] === dict[key]) {
        valueList.push(key);
      }
    }
    obj[newKeys[i]] = valueList;
    valueList = [];
  }
  console.log(obj);
}
organizeDict(dict);
