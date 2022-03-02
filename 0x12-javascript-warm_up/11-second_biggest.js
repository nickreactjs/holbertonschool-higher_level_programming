#!/usr/bin/node
/* Search the second biggest integer. */
const list = process.argv.slice(2);
let max = list[0];
let n, maxIndex;
let i = 0;
if (list.length === 0 || list.length === 1) {
  console.log('0');
} else {
  while (i < list.length) {
    n = parseInt(list[i]);
    if (n > max) {
      max = n;
      maxIndex = i;
    }
    i += 1;
  }
  list.splice(maxIndex, 1);
  i = 0;
  max = list[0];
  while (i < list.length) {
    n = parseInt(list[i]);
    if (n > max) {
      max = n;
    }
    i += 1;
  }
}
