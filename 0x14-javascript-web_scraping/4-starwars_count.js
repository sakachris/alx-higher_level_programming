#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    let count = 0;
    const movies = JSON.parse(body).results;
    for (const movie of movies) {
      for (const c of movie.characters) {
        if (c.includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
