#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const _body = JSON.parse(body);
  console.log(_body.title);
});
