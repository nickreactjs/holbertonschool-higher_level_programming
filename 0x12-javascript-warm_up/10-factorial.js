#!/usr/bin/node
function factorial (a) {
  /* Compute a factorial. */
  if (a === 1 || a === 0 || isNaN(a)) {
    return 1;
  }
  return (a * factorial(a - 1));
}

console.log(factorial(parseInt(process.argv[2])));
