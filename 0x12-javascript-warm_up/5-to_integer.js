#!/usr/bin/node
const number = parseInt(process.argv[2], 10);
let s;
if (isNaN(number)) {
  s = 'Not a number';
} else {
  s = 'My number: ' + number;
}
console.log(s);
