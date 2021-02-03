#!/usr/bin/node
const arg = process.argv[2];
let s;
if (arg === undefined) {
  s = 'No argument';
} else {
  s = arg;
}
console.log(s);
