#!/usr/bin/node

const myVar1 = process.argv[2];
const myVar2 = parseInt(myVar1, 10);
if (myVar2) {
  let square = '';
  for (let i = 0; i < myVar2; i++) {
    square += 'X';
  }
  for (let j = 0; j < myVar2; j++) {
    console.log(square);
  }
} else {
  console.log('Missing size');
}
