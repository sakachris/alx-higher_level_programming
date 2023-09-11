#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const myVar1 = process.argv[2];
const myInt1 = parseInt(myVar1, 10);

console.log(factorial(myInt1));
