#!/usr/bin/node

const firstArray = require('./100-data').list;
const secondArray = firstArray.map((value, index) => value * index);
console.log(firstArray);
console.log(secondArray);
