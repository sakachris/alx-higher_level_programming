#!/usr/bin/node

if (process.argv[2]) {
  const myVar = process.argv[2];
  console.log(myVar);
} else {
  console.log('No argument');
}
