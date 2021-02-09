#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const line = c.repeat(this.width) + '\n';
    process.stdout.write(line.repeat(this.width));
  }
};
