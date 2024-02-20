#!/usr/bin/node
const request = require('request');
const fs = require('node:fs');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(fileName, body, err => {
    if (err) {
      console.log(err);
    }
  });
});
