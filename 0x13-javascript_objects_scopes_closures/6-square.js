#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;
    let char;
    if (c == null) {
      char = 'X';
    } else {
      char = c;
    }
    while (i < this.height) {
      console.log(char.repeat(this.height));
      i += 1;
    }
  }
};
