#!/usr/bin/node
const size = parseInt(process.argv[2]);
let i = 0;
if (isNaN(size)) {
  console.log('Missing size');
}

while (i < size) {
  console.log('X'.repeat(size));
  i++;
}
