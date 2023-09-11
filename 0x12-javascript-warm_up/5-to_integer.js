#!/usr/bin/node

const myVar1 = process.argv[2];
const myVar2 = parseInt(myVar1, 10);
if (myVar2) {
  console.log('My number: ' + myVar2);
} else {
  console.log('Not a number');
}
