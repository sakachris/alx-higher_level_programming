#!/usr/bin/node

const firstDict = require('./101-data').dict;
const secondDict = {};

for (const key in firstDict) {
  secondDict[firstDict[key]] = [];
}
for (const key in firstDict) {
  secondDict[firstDict[key]].push(key);
}
console.log(secondDict);
