#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + id, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (err, response, body) {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
