#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let rect = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      rect += c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(rect);
    }
  }
};
