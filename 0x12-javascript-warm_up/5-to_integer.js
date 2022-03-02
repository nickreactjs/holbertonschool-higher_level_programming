#!/usr/bin/node
/* Print string. */
let argument = parseInt(process.argv[2]);
if (isNaN(argument)) {
  argument = 'Not a number';
}
console.log(argument);
