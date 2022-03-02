#!/usr/bin/node
/* Print X times C is fun. */
const number = parseInt(process.argv[2]);
let i = 0;
if (isNaN(number)) {
  console.log('Missing number of occurences');
} else {
  while (i < number) {
    console.log('C is fun');
    i += 1;
  }
}
