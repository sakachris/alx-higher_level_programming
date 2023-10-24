#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const done = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        if (!(task.userId in done)) {
          done[task.userId] = 1;
        } else {
          done[task.userId]++;
        }
      }
    }
    console.log(done);
  }
});
