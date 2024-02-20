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
    for (let j = 0; j < characters.length; j++) {
      const character = characters[j];
      const Id = character.split('/')[5];
      if (Id === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
