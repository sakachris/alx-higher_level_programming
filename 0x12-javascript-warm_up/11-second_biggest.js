#!/usr/bin/node

const myVar = process.argv.length;
if (myVar < 4) {
  console.log(0);
} else {
  let array = [];
  for (let i = 2; i < process.argv.length; i++) {
    array.push(parseInt(process.argv[i]));
    array = array.sort(function (a, b) {
      return a - b;
    });
  }
  console.log(array[array.length - 2]);
}
