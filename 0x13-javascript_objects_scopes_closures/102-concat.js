#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (errorA, contentA) => {
  if (errorA) {
    process.exit(1);
  }
  fs.readFile(fileB, 'utf8', (errorB, contentB) => {
    if (errorB) {
      process.exit(1);
    }
    const contentC = contentA + contentB;
    fs.writeFile(fileC, contentC, 'utf8', (errorC) => {
      if (errorC) {
        process.exit(1);
      }
    });
  });
});
