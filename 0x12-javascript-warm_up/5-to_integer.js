#!/usr/bin/node
const number = parseInt(process.argv[2], 10);
let s;
if (isNaN(number)) {
  s = 'Not a number';
} else {
  s = number;
}
console.log('My number: ' + s);
