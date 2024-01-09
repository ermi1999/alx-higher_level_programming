#!/usr/bin/node
const dict = require('./101-data.js').dict;
const obj = {};
const values = Object.values(dict);
for (let i = 0; i < values.length; i++) {
  obj[values[i]] = [];
}
const keys = Object.keys(dict);
for (let i = 0; i < keys.length; i++) {
  obj[dict[keys[i]]].push(keys[i]);
}
console.log(obj);
