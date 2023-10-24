#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filename, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      }
    });
  }
});
