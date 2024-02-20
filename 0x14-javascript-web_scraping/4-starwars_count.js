#!/usr/bin/node
const request = require('request');

let count = 0;
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const results = JSON.parse(body).results;
  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;
    if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
