#!/usr/bin/node

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const myVar1 = process.argv[2];
const myInt1 = parseInt(myVar1, 10);
const myVar2 = process.argv[3];
const myInt2 = parseInt(myVar2, 10);

add(myInt1, myInt2);
