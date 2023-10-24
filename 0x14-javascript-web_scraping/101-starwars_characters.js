#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const actors = JSON.parse(body).characters;

    function printOrder (i) {
      if (i < actors.length) {
        request(actors[i], function (err, response, body) {
          if (err) {
            console.error(err);
          } else {
            console.log(JSON.parse(body).name);
            printOrder(i + 1);
          }
        });
      }
    }
    printOrder(0);
  }
});
