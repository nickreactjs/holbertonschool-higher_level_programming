#!/usr/bin/node
/* Print a square. */
const number = parseInt(process.argv[2]);
let i = 0;
if (isNaN(number)) {
  console.log('Missing size');
} else {
  while (i < number) {
    console.log('X'.repeat(number));
    i += 1;
  }
}
