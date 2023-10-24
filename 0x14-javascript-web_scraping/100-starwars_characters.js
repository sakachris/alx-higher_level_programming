#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const actors = JSON.parse(body).characters;
    for (const actor of actors) {
      request(actor, function (err, response, body) {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
