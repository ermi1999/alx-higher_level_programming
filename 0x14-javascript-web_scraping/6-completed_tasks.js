#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  body = JSON.parse(body);
  const result = {};

  for (let i = 0; i < body.length; i++) {
    if (body[i].completed) {
      if (result[body[i].userId]) {
        result[body[i].userId]++;
      } else {
        result[body[i].userId] = 1;
      }
    }
  }
  console.log(result);
});
