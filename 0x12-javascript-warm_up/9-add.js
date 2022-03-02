#!/usr/bin/node
const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

function add (a, b) {
/* Print the addition of 2 integers. */
  return (parseInt(a) + parseInt(b));
}

console.log(add(n1, n2));
